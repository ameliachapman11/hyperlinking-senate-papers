<?php

use Twig\Environment;
use Twig\Error\LoaderError;
use Twig\Error\RuntimeError;
use Twig\Extension\CoreExtension;
use Twig\Extension\SandboxExtension;
use Twig\Markup;
use Twig\Sandbox\SecurityError;
use Twig\Sandbox\SecurityNotAllowedTagError;
use Twig\Sandbox\SecurityNotAllowedFilterError;
use Twig\Sandbox\SecurityNotAllowedFunctionError;
use Twig\Source;
use Twig\Template;
use Twig\TemplateWrapper;

/* core/modules/system/templates/system-themes-page.html.twig */
class __TwigTemplate_a6a552534ecb8c5c2829217db7267ffc extends Template
{
    private Source $source;
    /**
     * @var array<string, Template>
     */
    private array $macros = [];

    public function __construct(Environment $env)
    {
        parent::__construct($env);

        $this->source = $this->getSourceContext();

        $this->parent = false;

        $this->blocks = [
        ];
        $this->sandbox = $this->extensions[SandboxExtension::class];
    }

    protected function doDisplay(array $context, array $blocks = []): iterable
    {
        $macros = $this->macros;
        // line 34
        yield "<div";
        yield $this->extensions['Drupal\Core\Template\TwigExtension']->escapeFilter($this->env, ($context["attributes"] ?? null), "html", null, true);
        yield ">
  ";
        // line 35
        $context['_parent'] = $context;
        $context['_seq'] = CoreExtension::ensureTraversable(($context["theme_groups"] ?? null));
        foreach ($context['_seq'] as $context["_key"] => $context["theme_group"]) {
            // line 36
            yield "    ";
            // line 37
            $context["theme_group_classes"] = ["system-themes-list", ("system-themes-list-" . CoreExtension::getAttribute($this->env, $this->source,             // line 39
$context["theme_group"], "state", [], "any", false, false, true, 39)), "clearfix"];
            // line 43
            yield "    <div";
            yield $this->extensions['Drupal\Core\Template\TwigExtension']->escapeFilter($this->env, CoreExtension::getAttribute($this->env, $this->source, CoreExtension::getAttribute($this->env, $this->source, $context["theme_group"], "attributes", [], "any", false, false, true, 43), "addClass", [($context["theme_group_classes"] ?? null)], "method", false, false, true, 43), "html", null, true);
            yield ">
      <h2 class=\"system-themes-list__header\">";
            // line 44
            yield $this->extensions['Drupal\Core\Template\TwigExtension']->escapeFilter($this->env, CoreExtension::getAttribute($this->env, $this->source, $context["theme_group"], "title", [], "any", false, false, true, 44), "html", null, true);
            yield "</h2>
      ";
            // line 45
            $context['_parent'] = $context;
            $context['_seq'] = CoreExtension::ensureTraversable(CoreExtension::getAttribute($this->env, $this->source, $context["theme_group"], "themes", [], "any", false, false, true, 45));
            foreach ($context['_seq'] as $context["_key"] => $context["theme"]) {
                // line 46
                yield "        ";
                // line 47
                $context["theme_classes"] = [(((($tmp = CoreExtension::getAttribute($this->env, $this->source,                 // line 48
$context["theme"], "is_default", [], "any", false, false, true, 48)) && $tmp instanceof Markup ? (string) $tmp : $tmp)) ? ("theme-default") : ("")), (((($tmp = CoreExtension::getAttribute($this->env, $this->source,                 // line 49
$context["theme"], "is_admin", [], "any", false, false, true, 49)) && $tmp instanceof Markup ? (string) $tmp : $tmp)) ? ("theme-admin") : ("")), "theme-selector", "clearfix"];
                // line 54
                yield "        <div";
                yield $this->extensions['Drupal\Core\Template\TwigExtension']->escapeFilter($this->env, CoreExtension::getAttribute($this->env, $this->source, CoreExtension::getAttribute($this->env, $this->source, $context["theme"], "attributes", [], "any", false, false, true, 54), "addClass", [($context["theme_classes"] ?? null)], "method", false, false, true, 54), "html", null, true);
                yield ">
          ";
                // line 55
                if ((($tmp = CoreExtension::getAttribute($this->env, $this->source, $context["theme"], "screenshot", [], "any", false, false, true, 55)) && $tmp instanceof Markup ? (string) $tmp : $tmp)) {
                    // line 56
                    yield "            ";
                    yield $this->extensions['Drupal\Core\Template\TwigExtension']->escapeFilter($this->env, CoreExtension::getAttribute($this->env, $this->source, $context["theme"], "screenshot", [], "any", false, false, true, 56), "html", null, true);
                    yield "
          ";
                }
                // line 58
                yield "          <div class=\"theme-info\">
            <h3 class=\"theme-info__header\">";
                // line 60
                yield $this->extensions['Drupal\Core\Template\TwigExtension']->escapeFilter($this->env, CoreExtension::getAttribute($this->env, $this->source, $context["theme"], "name", [], "any", false, false, true, 60), "html", null, true);
                yield " ";
                yield $this->extensions['Drupal\Core\Template\TwigExtension']->escapeFilter($this->env, CoreExtension::getAttribute($this->env, $this->source, $context["theme"], "version", [], "any", false, false, true, 60), "html", null, true);
                // line 61
                if ((($tmp = CoreExtension::getAttribute($this->env, $this->source, $context["theme"], "notes", [], "any", false, false, true, 61)) && $tmp instanceof Markup ? (string) $tmp : $tmp)) {
                    // line 62
                    yield "                (";
                    yield $this->extensions['Drupal\Core\Template\TwigExtension']->renderVar($this->extensions['Drupal\Core\Template\TwigExtension']->safeJoin($this->env, CoreExtension::getAttribute($this->env, $this->source, $context["theme"], "notes", [], "any", false, false, true, 62), ", "));
                    yield ")";
                }
                // line 64
                yield "</h3>
            <div class=\"theme-info__description\">";
                // line 65
                yield $this->extensions['Drupal\Core\Template\TwigExtension']->escapeFilter($this->env, CoreExtension::getAttribute($this->env, $this->source, $context["theme"], "description", [], "any", false, false, true, 65), "html", null, true);
                yield "</div>
            ";
                // line 66
                if ((($tmp = CoreExtension::getAttribute($this->env, $this->source, $context["theme"], "module_dependencies", [], "any", false, false, true, 66)) && $tmp instanceof Markup ? (string) $tmp : $tmp)) {
                    // line 67
                    yield "              <div class=\"theme-info__requires\">
                ";
                    // line 68
                    yield $this->extensions['Drupal\Core\Template\TwigExtension']->renderVar(t("Requires: @module_dependencies", ["@module_dependencies" => $this->extensions['Drupal\Core\Template\TwigExtension']->renderVar(CoreExtension::getAttribute($this->env, $this->source, $context["theme"], "module_dependencies", [], "any", false, false, true, 68))]));
                    yield "
              </div>
            ";
                }
                // line 71
                yield "            ";
                // line 72
                yield "            ";
                if ((($tmp = CoreExtension::getAttribute($this->env, $this->source, $context["theme"], "incompatible", [], "any", false, false, true, 72)) && $tmp instanceof Markup ? (string) $tmp : $tmp)) {
                    // line 73
                    yield "              <div class=\"incompatible\">";
                    yield $this->extensions['Drupal\Core\Template\TwigExtension']->escapeFilter($this->env, CoreExtension::getAttribute($this->env, $this->source, $context["theme"], "incompatible", [], "any", false, false, true, 73), "html", null, true);
                    yield "</div>
            ";
                } else {
                    // line 75
                    yield "              ";
                    yield $this->extensions['Drupal\Core\Template\TwigExtension']->escapeFilter($this->env, CoreExtension::getAttribute($this->env, $this->source, $context["theme"], "operations", [], "any", false, false, true, 75), "html", null, true);
                    yield "
            ";
                }
                // line 77
                yield "          </div>
        </div>
      ";
            }
            $_parent = $context['_parent'];
            unset($context['_seq'], $context['_key'], $context['theme'], $context['_parent']);
            $context = array_intersect_key($context, $_parent) + $_parent;
            // line 80
            yield "    </div>
  ";
        }
        $_parent = $context['_parent'];
        unset($context['_seq'], $context['_key'], $context['theme_group'], $context['_parent']);
        $context = array_intersect_key($context, $_parent) + $_parent;
        // line 82
        yield "</div>
";
        $this->env->getExtension('\Drupal\Core\Template\TwigExtension')
            ->checkDeprecations($context, ["attributes", "theme_groups"]);        yield from [];
    }

    /**
     * @codeCoverageIgnore
     */
    public function getTemplateName(): string
    {
        return "core/modules/system/templates/system-themes-page.html.twig";
    }

    /**
     * @codeCoverageIgnore
     */
    public function isTraitable(): bool
    {
        return false;
    }

    /**
     * @codeCoverageIgnore
     */
    public function getDebugInfo(): array
    {
        return array (  153 => 82,  146 => 80,  138 => 77,  132 => 75,  126 => 73,  123 => 72,  121 => 71,  115 => 68,  112 => 67,  110 => 66,  106 => 65,  103 => 64,  98 => 62,  96 => 61,  92 => 60,  89 => 58,  83 => 56,  81 => 55,  76 => 54,  74 => 49,  73 => 48,  72 => 47,  70 => 46,  66 => 45,  62 => 44,  57 => 43,  55 => 39,  54 => 37,  52 => 36,  48 => 35,  43 => 34,);
    }

    public function getSourceContext(): Source
    {
        return new Source("", "core/modules/system/templates/system-themes-page.html.twig", "/var/www/html/web/core/modules/system/templates/system-themes-page.html.twig");
    }
    
    public function ensureSecurityChecked(): void
    {
        if ($this->sandbox->isSandboxed($this->source)) {
            $this->checkSecurity();
        }
    }
    
    public function checkSecurity()
    {
        static $tags = ["for" => 35, "set" => 37, "if" => 55];
        static $filters = ["escape" => 34, "safe_join" => 62, "t" => 68, "render" => 68];
        static $functions = [];

        try {
            $this->sandbox->checkSecurity(
                [0 => "for", 1 => "set", 2 => "if"],
                [0 => "escape", 1 => "safe_join", 2 => "t", 3 => "render"],
                [],
                $this->source
            );
        } catch (SecurityError $e) {
            $e->setSourceContext($this->source);

            if ($e instanceof SecurityNotAllowedTagError && isset($tags[$e->getTagName()])) {
                $e->setTemplateLine($tags[$e->getTagName()]);
            } elseif ($e instanceof SecurityNotAllowedFilterError && isset($filters[$e->getFilterName()])) {
                $e->setTemplateLine($filters[$e->getFilterName()]);
            } elseif ($e instanceof SecurityNotAllowedFunctionError && isset($functions[$e->getFunctionName()])) {
                $e->setTemplateLine($functions[$e->getFunctionName()]);
            }

            throw $e;
        }

    }
}
