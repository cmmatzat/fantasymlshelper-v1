<!DOCTYPE html>
<html>
  <head>
    <title>FMH - Schedule</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
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
      
      function get_time($time)
      {
        $date_obj = DateTime::createFromFormat("YY-MM-DD HH:II:SS tzcorrection?", $time);
        $game_time = $date_obj->format("HH:II");
        return $game_time;
      }
      
      foreach ($schedule as $round) : ?>
      <div class="round flex-row">
        <div class="round-header">ROUND <?php echo $round['round']; ?></div>
      <?php foreach ($round['matches'] as $match) : ?>
        <div class="match">
          <div class="match-date <?php echo $match['time']['day_of_week'] ?>"><?php echo $match['time']['date']; ?></div>
          <div class="match-body flex-col">
            <div class="match-time"><?php echo $match['time']['time']; ?></div>
            <div class="match-img-box">
              <img src="https://d1j2t3dnax9fm.cloudfront.net/media/mls_mls/squads/logos/<?php echo $match['home_squad']['id'] ?>.png" alt="<?php echo $match['home_squad']['short_name'] ?>">
              <div class="match-text">v</div>
              <img src="https://d1j2t3dnax9fm.cloudfront.net/media/mls_mls/squads/logos/<?php echo $match['away_squad']['id'] ?>.png" alt="<?php echo $match['away_squad']['short_name'] ?>">
            </div>
          </div>
        </div>
      <?php endforeach; ?>
      </div>
    <?php endforeach; ?>
    </div>
  </body>
</html>