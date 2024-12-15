$Data = Get-Content -Path C:\Users\kyled\Desktop\github\advent_of_code\2024-AdventOfCode\day13\sample.txt

#$Data.GetType()
#$Data

# array for config data
$completed_configs = @()
$coordinates = @()


foreach($line in $Data) {

    if($line.Contains("Button A:"))
    {
        $A = $line.Split()
        $AX = $A[2] -replace ",",""
        $AX = [int]$AX.replace("X+", "")
        $AY = [int]$A[3].replace("Y+","")

        $coordinates += @{
        AX = $AX
        AY = $AY
        }

        $coordinates
        Write-Output "Parsed $A -> ($AX,$AY)"
    }

    elseif($line.Contains("Button B:"))
    {
        $B = $line.Split()
        $BX = $B[2] -replace ",",""
        $BX = [int]$BX.replace("X+", "")
        $BY = [int]$B[3].replace("Y+","")

        $coordinates += @{
            BX = $BX
            BY = $BY
        }

        Write-Output "Parsed $B -> ($BX, $BY)"
    }

    elseif($line.Contains("Prize:"))
    {
        $P = $line.Split()
        $PX = $P[1] -replace ",",""
        $PX = [int]$PX.replace("X=","")
        $PY = [int]($P[2] -replace "Y=","")
        $coordinates += @{
            PX = $PX
            PY = $PY
        }
        Write-Output "Parsed $P -> ($PX, $PY)"
    }

    elseif($line -eq "")
    {
        Write-Output "
------ Processing Game ------
        "
        $coordinates
        # reset after processing
        $completed_configs += $coordinates
        $coordinates = @()
    }

}
