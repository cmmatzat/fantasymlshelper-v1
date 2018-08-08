<?php
  // Load config file
  require_once($_SERVER["DOCUMENT_ROOT"]."/resources/config.php");

  
  // Load header template
  require_once(TEMPLATES_PATH . "/header.php");
?>

    <div id="page-content">
    </div>
<?php
  require_once(TEMPLATES_PATH . "/footer.php");
?>