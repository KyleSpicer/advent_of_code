<#
.SYNOPSIS
Union Find - Disjoint Set Union
- Disjoint meaning non-overlapping sets
- maintains a collection of elements split into disjoint sets
#>

class DSU {
    # $Parent stores the parent node i in a tree structure
    [int[]]$Parent
    # Every set is represented as a tree with one root
    [int[]]$Size

    # constructor, creates DSU with n elements
    DSU([int]$n) {
        # initialize each element as its own parent
        # every element starts in its own set
        $this.Parent = 0..($n - 1)

        # initialize every set to size 1
        $this.Size = @(for ($i = 0; $i -lt $n; $i++) { 1 })
    }

    # Finds which set an element belongs to
    # Find with path compression
    # Finds and returns the root of the set containing element x
    [int] Find([int]$x) {
        # if x is not a root
        if ($this.Parent[$x] -ne $x) {
            # recursively find the root and
            # update x's parent to point directly to that root
            $this.Parent[$x] = $this.Find($this.Parent[$x])
        }
        # return the root of the set
        return $this.Parent[$x]
    }

    # merges two sets together
    # attempts to merge the sets containing a and b
    # returns true if merge happened
    # returns false if already in the same set
    [bool] Union([int]$a, [int]$b) {
        # find the roots of both elements
        $ra = $this.Find($a)
        $rb = $this.Find($b)

        # if both elements have the same root
        # they are already connected, no merge needed
        if ($ra -eq $rb) { return $false }

        # compare sizes of the two sets
        # attach the smaller tree under the larger one
        # keeps trees shallow for faster finds
        if ($this.Size[$ra] -lt $this.Size[$rb]) {
            # attach root and update size
            $this.Parent[$ra] = $rb
            $this.Size[$rb] += $this.Size[$ra]
        }
        else {
            # attach root and update size
            $this.Parent[$rb] = $ra
            $this.Size[$ra] += $this.Size[$rb]
        }
        return $true
    }
}