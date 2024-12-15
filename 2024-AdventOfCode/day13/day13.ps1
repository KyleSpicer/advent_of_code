$Data = Get-Content -Path C:\Users\kyled\Desktop\github\advent_of_code\2024-AdventOfCode\day13\sample.txt

#$Data.GetType()
#$Data

# temp hash table for each game
$game = @{}

$game_count = 0
$total_button_presses = 0

foreach($line in $Data) {

    if($line.Contains("Button A:"))
    {
        $A = $line.Split()
        $AX = $A[2] -replace ",",""
        $AX = [int]$AX.replace("X+", "")
        $AY = [int]$A[3].replace("Y+","")

        $game['AX'] = $AX
        $game['AY'] = $AY

    }

    elseif($line.Contains("Button B:"))
    {
        $B = $line.Split()
        $BX = $B[2] -replace ",",""
        $BX = [int]$BX.replace("X+", "")
        $BY = [int]$B[3].replace("Y+","")

        $game['BX'] = $BX
        $game['BY'] = $BY

    }

    elseif($line.Contains("Prize:"))
    {
        $P = $line.Split()
        $PX = $P[1] -replace ",",""
        $PX = [int]$PX.replace("X=","")
        $PY = [int]($P[2] -replace "Y=","")

        $game['PX'] = $PX
        $game['PY'] = $PY

    }

    elseif($line.Trim() -eq "")
    {
        $game_count++
        Write-Output "------ Processing Game #$game_count------"
        $game

        $a_button_presses = ($game['PX'] * $game['BY'] - $game['PY'] * $game['BX']) / ($game['AX'] * $game['BY'] - $game['AY'] * $game['BX'])
        $b_button_presses = ($game['PX'] - $game['AX'] * $a_button_presses) / $game['BX']


        $a = $a_button_presses % 1
        $b = $b_button_presses % 1

        if ($a -eq $b)
        {
            if ($b -eq 0)
            {
                $total_button_presses += ($a_button_presses * 3) + $b_button_presses
            }
        }


        # reset after processing
        $game = @{}
    }

}

Write-Output "Part One Answer = $total_button_presses"
