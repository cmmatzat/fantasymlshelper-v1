<!DOCTYPE html>
<html>
  <head>
    <title>FMH - Schedule</title>
    <link rel="stylesheet" type="text/css" href="style/schedule.css"/> 
    <link rel="stylesheet" type="text/css" href="style/nav.css"/>
  </head>
  <body>
    <nav>
      <div><a href="index.php">HOME</a></div>
      <div><a href="schedule.php">SCHEDULE</a></div>
    </nav>
    <div class="schedule-container">
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
      
      foreach ($schedule as $round) : ?>
      <div class="round">
        <div class="round-header">ROUND <?php echo $round['round']; ?></div>
      <?php foreach ($round['matches'] as $match) : ?>
        <div class="match">
          <div class="match-img-box">
            <img src="https://d1j2t3dnax9fm.cloudfront.net/media/mls_mls/squads/logos/<?php echo $match['home_squad']['id'] ?>.png" alt="<?php echo $match['home_squad']['short_name'] ?>">
            <div class="match-text">v</div>
            <img src="https://d1j2t3dnax9fm.cloudfront.net/media/mls_mls/squads/logos/<?php echo $match['away_squad']['id'] ?>.png" alt="<?php echo $match['away_squad']['short_name'] ?>">
          </div>
        </div>
      <?php endforeach; ?>
      </div>
    <?php endforeach; ?>
    </div>
  </body>
</html>