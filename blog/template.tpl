{%- extends 'full.tpl' -%}

{% block header %}
{{ super() }}

<!-- Mobile design -->
<meta name="viewport" content="width=device-width, initial-scale=1">

<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-144706135-1"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'UA-144706135-1');
</script>

<!--Experiment-->
<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.4/jquery.min.js"></script>
<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.4/jquery-ui.min.js"></script>
<link rel="stylesheet" type="text/css" href="dist/overhang.min.css" />
<script type="text/javascript" src="dist/overhang.min.js"></script>

<!-- Anti-flicker snippet (recommended)  -->
<style>.async-hide { opacity: 0 !important} </style>
<script>(function(a,s,y,n,c,h,i,d,e){s.className+=' '+y;h.start=1*new Date;
h.end=i=function(){s.className=s.className.replace(RegExp(' ?'+y),'')};
(a[n]=a[n]||[]).hide=h;setTimeout(function(){i();h.end=null},c);h.timeout=c;
})(window,document.documentElement,'async-hide','dataLayer',4000,
{'GTM-T3QBCMS':true});</script>
<!-- Modified Analytics tracking code with Optimize plugin -->
<script>
    (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
    (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
    m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
    })(window,document,'script','https://www.google-analytics.com/analytics.js','ga');

    ga('create', 'UA-144706135-1', 'auto');
    ga('require', 'GTM-T3QBCMS');
    ga('send', 'pageview');
    
</script>

<!--script src="dist/jquery.progressScroll.min.js"></script-->
<!--link rel="stylesheet" href="dist/custom.css"-->
<script src="dist/VerLim.min.js"></script>
<link rel="stylesheet" href="dist/themeNUIwithCounter.css">
<script>
	jQuery(document).ready(function () {
	$(window).VerLim(
		{
			autoHide: "on",
			autoHideTime: "2",
			theme: "off",
			position: "top",
			thickness: "10px",
			shadow: "on"
		});
	})
</script>

{% endblock header %}
