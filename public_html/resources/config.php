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
    )
  );
  
  
  // Constants for heavily-used paths
  defined("LIBRARY_PATH") or define("LIBRARY_PATH", realpath(dirname(__DIR__) . '/library'));
  defined("TEMPLATES_PATH") or define("TEMPLATES_PATH", realpath(dirname(__DIR__) . '/templates'));
?>