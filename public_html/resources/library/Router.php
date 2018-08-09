<?php
    class Router
	{
		public function __construct()
		{

		}

		public function route($raw_uri)
		{
			$request_uri = explode('?', $raw_uri, 2);

		    switch ($request_uri[0])
		    {
		        // Home page
		        case '/':
		            $model = new Model();
					$controller = new Controller($model);
					$view = new View($controller, $model);
					echo $view->output();
		            break;
		        // About page
		        case '/schedule':
		            require 'views/schedule.php';
		            break;
		        // Everything else
		        default:
		            header('HTTP/1.0 404 Not Found');
		            require 'views/404.php';
		            break;
    		}
		}
	}
?>