{% extends 'lab/index.html.j2' %}

{% block header %}
{{ super() }}


<!-- MathJax.js -->
<!-- https://stackoverflow.com/questions/26275645/how-to-support-latex-in-github-pages/46765337#46765337 -->
<script type="text/x-mathjax-config">
    MathJax.Hub.Config({
      tex2jax: {
        skipTags: ['script', 'noscript', 'style', 'textarea', 'pre'],
        inlineMath: [['$','$']]
      }
    });
</script>
<script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>

<!-- Mobile design -->
<!--meta name="viewport" content="width=device-width, initial-scale=1"-->
<style>
@media only screen and (max-width: 500px) {
    .jp-InputPrompt.jp-InputArea-prompt{
        display: none;
    }
    .jp-OutputPrompt.jp-OutputArea-prompt{
        display: none;
    }
}
</style>

{% endblock header %}
