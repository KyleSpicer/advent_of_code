<#
.SYNOPSIS
Advent of Code 2025, Day 6
#>

function Get-MathProblems {
    param(
        [string]$Path
    )

    # parse data as arrays of strings
    $Data = Get-Content -Path $Path | ForEach-Object { , ($_.Trim() -split '\s+') }
    
    # number of items per line
    $totalProblems = $Data[0].Count
    $totalLines = $Data.Count
    
    # create empty arrays for numbers/symbols
    $problemsArray = @()
    
    # loop over each column to grab full problem
    for ($col = 0; $col -lt $totalProblems; $col++) {
        $columnArray = @()

        # loop over each row in the original data
        for ($row = 0; $row -lt $totalLines; $row++) {
            
            $currChar = $Data[$row][$col]

            # convert numbers to uint64
            if ($currChar -match '^\d+$') {
                $value = [uint64]$currChar
            }
            else {
                $value = $currChar
            }

            # add $value to $columnArray
            $columnArray += $value
        }

        # add complete column array to $problemsArray
        $problemsArray += , $columnArray
    }
    
    return $problemsArray
}

function Get-MathProblems2 {
    param(
        [string]$Path
    )

    # parse data as arrays of strings
    $Data = Get-Content -Path $Path | ForEach-Object { , $_.ToCharArray() }

    $answer = 0
    $results = @()
    $operator = ''

    for ($c = 0; $c -lt $Data[0].Count; $c++) {

        # retrieve operator
        $bottomChar = $Data[$Data.Count - 1][$c]
        if ($bottomChar -ne ' ') {
            $operator = $bottomChar
        }

        # collect the column's characters
        $colChars = for ($r = 0; $r -lt $Data.Count - 1; $r++) {
            $Data[$r][$c]
        }

        $digits = ($colChars -join '') -replace '\s', ''

        if ($digits) {
            $value = [uint64]$digits
            $results += $value
        }
        else {
            # process the problem
            if ($results.Count -gt 0) {
                $total = $results[0]
                for ($i = 1; $i -lt $results.Count; $i++) {
                    switch ($operator) {
                        '+' { $total += $results[$i] }
                        '*' { $total *= $results[$i] }
                    }
                }
                $answer += $total
                $results = @()
                $operator = ''
            }
        }
    }        

    # process remaining numbers
    if ($results.Count -gt 0) {
        $total = $results[0]
        for ($i = 1; $i -lt $results.Count; $i++) {
            switch ($operator) {
                '+' { $total += $results[$i] }
                '*' { $total *= $results[$i] }
            }
        }
        $answer += $total
    }

    return $answer
}

function Get-PartOne {
    param(
        [object[][]]$Data
    )

    $total = 0

    foreach ($problem in $Data) {

        $operator = $problem[-1]
        $numbers = $problem[0..($problem.Count - 2)]

        switch ($operator) {
            '*' { $results = 1 }
            '+' { $results = 0 }
        }

        foreach ($num in $numbers) {
            switch ($operator) {
                '*' { $results *= $num }
                '+' { $results += $num }
            }
        }

        $total += $results

    }

    return $total
}

$sample = ".\sample.txt"
$inputFile = ".\input.txt"

$Data = Get-MathProblems -Path $inputFile
$partOneDuration = Measure-Command { $partOne = Get-PartOne -Data $Data }
Write-Host "[+] Part One: $partOne ($($partOneDuration.TotalSeconds) seconds)"

$partTwoDuration = Measure-Command { $partTwo = Get-MathProblems2 -Path $inputFile }
Write-Host "[+] Part Two: $partTwo ($($partTwoDuration.TotalSeconds) seconds)"


