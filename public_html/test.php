<?php
  // Load config file
  require_once($_SERVER["DOCUMENT_ROOT"] . "/resources/config.php");
  
  // Load header template
  require_once(TEMPLATES_PATH . "/header.php");
?>
    <div id="page-content" class="flex-col-top shadow">
    <?php
      $url='https://data.fantasymlshelper.com/data/schedule/schedule.json';
      $response = get_json_data($url);
      $schedule = json_decode($response, true);

      function get_json_data($url)
      {
        $ch = curl_init();
        $timeout = 5;
        curl_setopt($ch,CURLOPT_URL,$url);
        curl_setopt($ch,CURLOPT_RETURNTRANSFER,1);
        curl_setopt($ch,CURLOPT_CONNECTTIMEOUT,$timeout);
        $data = curl_exec($ch);
        curl_close($ch);
        return $data;
      }
      
      // Create a section of the page for each round
      foreach ($schedule as $round) : ?>
      <!--<div class="section flex-col-top flex-grow">-->
      
        <?php // The first row of the section is a header bar with the round number ?>
        <!--<div class="sch-round-header flex-grow">ROUND <?php echo $round['round']; ?></div>-->
        
        <?php // The second row is a container for matches ?>
        <div class="section flex-grow flex-row">
        
        <?php 
          // Each match itself is a flexbox with a header and body
          foreach ($round['matches'] as $match) : ?>
          <!--<div class="sch-match flex-col-top-nowrap flex-strict shadow">-->
          
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
          <!--</div>-->
          <?php endforeach; ?>
        <!--</div>-->

        <?php // The third row is a container for DGW/BYE teams ?>
              
      <!--</div>-->
    <?php endforeach; ?>
    </div>
<?php
  require_once(TEMPLATES_PATH . "/footer.php");
?>