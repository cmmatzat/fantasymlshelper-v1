<?php
    function make-sch-match-box($match)
    {
        <div class="sch-match flex-col-top-nowrap flex-strict shadow">
          
            <?php // Match header sits on top with the date ?>
            <div class="sch-match-header flex-strict <?php echo $match['time']['day_of_week'] ?>"><?php echo $match['time']['date']; ?></div>
            <?php // Match body contains other items in a column ?>
            <div class="sch-match-body flex-col flex-shrink">
            
              <?php // First item is the time ?>
              <div class="sch-match-time flex-strict"><?php echo $match['time']['time']; ?></div>
              <?php // Second item is a row of logos ?>
              <div class="sch-match-matchup section flex-strict flex-row-space">
                <img class="flex-strict" src="https://d1j2t3dnax9fm.cloudfront.net/media/mls_mls/squads/logos/<?php echo $match['home_squad']['id'] ?>.png" alt="<?php echo $match['home_squad']['short_name'] ?>">
                <div class="flex-strict">v</div>
                <img class="flex-strict" src="https://d1j2t3dnax9fm.cloudfront.net/media/mls_mls/squads/logos/<?php echo $match['away_squad']['id'] ?>.png" alt="<?php echo $match['away_squad']['short_name'] ?>">
              </div>
            </div>
          </div>
    }
?>