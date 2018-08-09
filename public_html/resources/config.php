<?php
  
  /*
    This config file is used to set paths for the project.
  */
  
  $config = array(
    "paths" => array(
      "resources" => $_SERVER["DOCUMENT_ROOT"]."/resources",
      "images" => $_SERVER["DOCUMENT_ROOT"]."/img"
    ),
    "urls" => array(
      "serverBase" => "https://data.fantasymlshelper.com",
      "schedule" => "https://data.fantasymlshelper.com/data/schedule/schedule.json"
    ),
    "libs" => array(
      "Container"
    )
  );
  
  // Constants for heavily-used paths
  defined('TEMPLATES_PATH') or define('TEMPLATES_PATH', $_SERVER["DOCUMENT_ROOT"] . '/resources/templates');
  defined('LIBRARY_PATH') or define('LIBRARY_PATH', $_SERVER["DOCUMENT_ROOT"] . '/resources/library');
  defined('VIEWS_PATH') or define('VIEWS_PATH', $_SERVER["DOCUMENT_ROOT"] . '/views');

  // Include custom classes
  include_once(LIBRARY_PATH . '/Model.php');
  include_once(LIBRARY_PATH . '/View.php');
  include_once(LIBRARY_PATH . '/Controller.php');
  include_once(LIBRARY_PATH . '/Router.php');
?>