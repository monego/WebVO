<?php include($_SERVER['DOCUMENT_ROOT']."/include/functions.php"); ?>

<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" lang="pt-br" dir="ltr">
<head>
	<title>INPE/Modelo Padrão</title>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	<meta content="width=device-width, initial-scale=1.0" name="viewport" />

	<link rel="shortcut icon" href="/img/favicon.ico" type="image/x-icon" />
	<link rel="apple-touch-icon" href="/img/favicon.png" />

	<link media="screen" href="/css/plone.css" type="text/css" rel="stylesheet" id="plone-css" />    
	<link media="all" href="/css/main.css" type="text/css" rel="stylesheet" id="main-css" />  
	<link media="all" href="/css/style.css" type="text/css" rel="stylesheet" id="style-css" />

	<link media="all" href="/css/css-intranet-inpe.css" rel="stylesheet" id="intranet-css" /> 
	<link media="all" href="/css/css-menu.css" rel="stylesheet" id="menu-css" />    

	<!-- CONTRASTE -->
	<link media="all" href="/css/css-intranet-inpe-contraste.css" rel="stylesheet" id="intranet-css-contraste" /> 
	<link media="all" href="/css/css-menu-contraste.css" rel="stylesheet" id="menu-css-contraste" />   

	<script src="/js/jquery/jquery-1.9.1.js" type="application/javascript"></script>  
	<script src="/js/jquery/jquery.cookie.js" type="application/javascript"></script>  
	<script src="/js/functions.js" type="application/javascript"></script>


</head>

<body>
	<!-- TOPO -->    
	<?php include($_SERVER['DOCUMENT_ROOT']."/topo.php"); ?>


	<!-- CONTEUDO -->
	<div id="main" role="main">
		<div id="plone-content">

			<div id="portal-columns" class="row">

				<!-- RASTRO -->
				<div id="viewlet-above-content">
					<div id="portal-breadcrumbs">
						<span id="breadcrumbs-you-are-here">
							Você está aqui: 
							<span>
								<?= rastro();?>
							</span>
						</span>
					</div>
				</div>


				<!-- Column 1 - MENU -->      
				<?php include($_SERVER['DOCUMENT_ROOT']."/menu.php"); ?>	

				<!-- Conteudo -->
				<div id="portal-column-content" class="cell width-3:4 position-1:4">

					<div id="main-content">    
						<div id="content">

							<h1 class="documentFirstHeading">Modelo Padrão</h1>
                            
							<div class="documentByLine">
								<span class="documentAuthor">Publicado Por: <a href="/" title="Acesse Publicado Por">INPE</a></span>
								<?= dataModificacao();?>
							</div>

							<h2>Sobre</h2>
                            <br />
                            <strong>INPE + Governo Federal</strong>

							<br><br>
                            
                            <p>Modelo padrão para confecção de sites do INPE que segue o modelo do Governo Federal e suas diretrizes para garantir o amplo acesso à informação através da internet.</p>
                            
                            <p>Este modelo é destinado a páginas institucionais de Divisão, Seção/ Setor, Núcleo, Laboratório Associado, Centro Regional, Unidade Regional, entre outras.</p>
                            
                            <p>O conteúdo deve estar disponível de forma padronizada e de fácil navegação, conforme estabelecido pela SECOM e sua área de e-GOV.
                            </p>
                            
                            <p>
                            <strong><em>
                            	Coordenação de Tecnologia da Informação - COCTI<br>
								Serviço de Tecnologia da Informação - SCSTI                               
                            </em></strong>
                            </p>
                            
                            <p>
                            <strong>Desenvolvido por <a href="/ti/" title="Acesse COCTI/INPE">COCTI/INPE</a></strong>
                            </p>
							
                            <div class="clear"></div>


						</div>
					</div>
				</div>
				<!-- Fim do Conteudo -->            


				<div class="clear"><!-- --></div>
				<div id="voltar-topo"><a href="#topo" title="Acesse Voltar para o topo">Voltar para o topo</a></div>


			</div>
		</div>
	</div>
	<!-- FIM CONTEUDO -->

	<div class="clear"><!-- --></div>

	<!-- Footer -->
	<?php include($_SERVER['DOCUMENT_ROOT']."/rodape.php"); ?>
	<!-- /Footer-->

</body>  
</html>
