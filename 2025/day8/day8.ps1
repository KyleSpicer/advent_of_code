<#
.SYNOPSIS
Advent of Code 2025 Day 8

.DESCRIPTION
Junction Box = Node (vertex)
Cable = Edge (every possible pair of boxes)
Distance = Edge weight (distance between them)

Kruskal's Algorithm answers:
- "What is the cheapest way to connect everything 
                             without making pointless loops"

1. sort all edges (distances) from shortest to longest
2. start with 0 connections
3. iterate through edges in order
    - if edge connects two different groups, keep it
    - if it would form a loop, skip it
4. stop when everything is connected

Disjoint Set Union answers, "Are these two boxes already connected somehow?"
- keeps track of which boxes are in which group
- Find(x) tells you which group x belongs to
- Union(a, b) merges two groups if they were different
- Path compression flattens the structure
- Union by size keeps tree shallow
#>

. ".\DisjointUnionSet.ps1"

function Get-JunctionBoxes {
    param(
        [string]$Path
    )

    $points = Get-Content -Path $Path | ForEach-Object {
        $x, $y, $z = $_ -split ','
        [PSCustomObject]@{
            X = [int]$x
            Y = [int]$y
            Z = [int]$z
        }
    }

    return $points
}

function Get-Edges {
    param(
        [Object[]]$Data
    )

    # stores all possible connections (edges) between boxes
    $edges = New-Object 'System.Collections.Generic.List[System.Object]'
    $boxCount = $Data.Count

    # 1. generate distances and store them
    for ($i = 0; $i -lt $boxCount; $i++) {
        for ($j = $i + 1; $j -lt $boxCount; $j++) {
            $a = $Data[$i]
            $b = $Data[$j]

            $dx = $b.X - $a.X
            $dy = $b.Y - $a.Y
            $dz = $b.Z - $a.Z

            # squared distance preserves ordering
            # avoids expensive sqrt() calls
            # sorting by distance (D) gives same result as sorting by real distance
            $edges.Add([PSCustomObject]@{
                    I = $i
                    J = $j
                    D = ($dx * $dx + $dy * $dy + $dz * $dz) # squared distance
                })
        }
    }

    return $edges
}

function Get-PartOne {
    param (
        [Object[]]$Data # junction box coordinates
    )

    # stores all possible connections (edges) between boxes
    $edges = Get-Edges -Data $Data

    # 2. sort and union first 10 or 1000 edges
    # sort by distance, orders all possible connections from shortest to longest
    $edges = $edges | Sort-Object D
    $dsu = [DSU]::new($boxCount)

    # each junction box starts as its own circuit
    # take the shortest remaining edge
    # connect the two junction boxes, if the are not already connected
    # DSU silently ignores redundant connections
    # this is Kruscal's algorithm, but stop after $Size edges instead of a full MST (Minimum Spanning Tree)
    for ($k = 0; $k -lt $boxCount; $k++) {
        $e = $edges[$k]
        $dsu.Union($e.I, $e.J) | Out-Null
    }

    # 3. compute circuit sizes
    $counts = @{}
    for ($i = 0; $i -lt $boxCount; $i++) {
        $root = $dsu.Find($i)
        if (-not $counts.ContainsKey($root)) {
            $counts[$root] = 0
        }
        $counts[$root]++
    }

    # 4. multiply top three for answer
    $topThree = $counts.Values | Sort-Object -Descending | Select-Object -First 3

    $result = 1
    $topThree | ForEach-Object { $result *= $_ }
    return $result
}

function Get-PartTwo {
    param (
        [Object[]]$Data # junction box coordinates
    )

    # 1. Get edges
    $edges = Get-Edges -Data $Data

    # 2. sort edges by distance
    $edges = $edges | Sort-Object D

    # 3. Kruskal until fully connected
    $dsu = [DSU]::new($Data.Count)
    $components = $Data.Count

    foreach ($e in $edges) {
        if ($dsu.Union($e.I, $e.J)) {
            $components--
        }

        # This edge makes the whole graph connected
        if ($components -eq 1) {
            $a = $Data[$e.I]
            $b = $Data[$e.J]
            return $a.X * $b.X
        }
    }

    throw "[!] Graph never became fully connected"
}

$sampleFile = ".\sample.txt"
$inputFile = ".\input.txt"

$junctionBoxes = Get-JunctionBoxes -Path $inputFile

$partOneTime = Measure-Command { $partOne = Get-PartOne -Data $junctionBoxes }
Write-Host "[+] Part One: $partOne ($($partOneTime.TotalSeconds) seconds)"

$partTwoTime = Measure-Command { $partTwo = Get-PartTwo -Data $junctionBoxes }
Write-Host "[+] Part Two: $partTwo ($($partTwoTime.TotalSeconds) seconds)"