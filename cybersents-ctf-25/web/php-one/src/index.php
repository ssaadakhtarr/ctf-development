<?php 

$page = $_GET["page"];

if (isset($page)) {
    include("page/" . $page);
} else {
    echo "Nothing to show you!";
}

?>