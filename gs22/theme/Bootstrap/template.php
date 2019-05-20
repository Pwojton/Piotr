<?php if(!defined('IN_GS')){ die('you cannot load this page directly.'); } ?>
<!DOCTYPE html>
<html lang="pl">

<head>
   <meta charset="utf-8">
   <meta name="viewport" content="width=device-width, initial-scale=1">
   <meta http-equiv="x-ua-compatible" content="ie=edge">
   <title><?php get_page_clean_title(); ?> &lt; <?php get_site_name(); ?></title>
   <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
   <link rel="stylesheet" href="<?php get_theme_url(); ?>/klasa.css" media="all" />
   <?php get_header(); ?>
</head>

<body>
   <header>
      <div class="container-fluid text-center">
         <h1><?php get_site_name(); ?><br><span class="text-muted small">Serwis klasy 1A I LO</span></h1>
      </div>
   </header>
   <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <a class="navbar-brand" href="#">Nasza klasa</a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#nawigacja" aria-controls="nawigacja" aria-expanded="false" aria-label="Toggle navigation">
         <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="nawigacja">
         <ul class="navbar-nav m-auto">
            <?php get_i18n_navigation(return_page_slug(), 0, 0, I18N_SHOW_NORMAL, $component='bs_menu'); ?>
         </ul>
         <form class="form-inline my-2 my-lg-0">
            <input class="form-control mr-sm-2" type="search" placeholder="Szukaj" aria-label="Szukaj">
            <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Szukaj</button>
         </form>
      </div>
   </nav>
   <div class="container">
      <div class="row">
         <div class="col-md-8">
            <section class="my-4">
               <h2><?php get_page_title(); ?></h2>
               <?php get_page_content(); ?>
            </section>
         </div>
         <div class="col-md-4">
            <aside class="rounded p-2 text-md-right my-1 my-md-4">
               <h3>Zobacz również</h3>
               <?php get_component('sidebar')?>
            </aside>
         </div>
      </div>
   </div>

   <?php get_footer();?>
   <!-- jQuery library -->
   <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
   <!-- Popper JS -->
   <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
   <!-- Latest compiled JavaScript -->
   <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
</body>

</html>
