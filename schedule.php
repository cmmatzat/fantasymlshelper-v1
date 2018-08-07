<!DOCTYPE html>
<html>
  <head>
    <title>FMH - Schedule</title>
    <link rel="stylesheet" type="text/css" href="style/schedule.css"/> 
  </head>
  <body>
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
    ?>

    <?php foreach ($schedule as $round) : ?>
      <div class="round">
        <div class="round-header">ROUND <?php echo $round['round']; ?> </div>
      <?php foreach ($round['matches'] as $match) : ?>
        <div class="match"><?php echo $match['home_squad']['short_name'] ?><br>v<br><?php echo $match['away_squad']['short_name'] ?></div>
      <?php endforeach; ?>
      </div>
    <?php endforeach; ?>
    </div>
  </body>
</html>