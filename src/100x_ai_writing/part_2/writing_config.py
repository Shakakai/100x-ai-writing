from typing import Optional, Literal, ClassVar, List
from typedtemplate import JinjaTemplateEngine, TypedTemplate, BaseTemplateEngine


engine = JinjaTemplateEngine()


class ExampleWriting(TypedTemplate):
    engine: ClassVar[BaseTemplateEngine] = engine
    template_string: ClassVar[str] = """
## Examples
Follow these examples to craft your response:
{% for example in examples %}
### Example
{{ example }}
{% endfor %}
    """

    examples: List[str]


class WritingStyle(TypedTemplate):
    engine: ClassVar[BaseTemplateEngine] = engine
    template_string: ClassVar[str] = """
## Writing Style
Reading Level: {% if reading_level == "simple" }Grade 6 or below{% elif reading_level == "general" %}Grade 12 or below{% else %}College level or above{% endif %}
{% if allow_passive_voice %}
You may use passive voice when appropriate.
{% else %}
Passive voice is not allowed.
{% endif %}

{% if allow_split_inifitives %}
You may use split infinitives when it improves clarity.
{% else %}
You may not use split infinitives.
{% endif %}

{% if allow_wordiness %}
You may use more words to explain complex concepts thoroughly if needed.
{% else %}
Minimize your wordiness.
{% endif %}

{% if enforce_confidence %}
Must use confident language and avoid hedging or uncertain language.
{% endif %}

{% if use_inclusive_gender %}
You must use gender-inclusive pronouns and nouns.
{% endif %}

{% if avoid_sensitive_topics %}
You must steer clear of controversial or potentially offensive subjects including:
- Disability
- Age
- Gender Identity
- Race, Ethnicity, and nationality
- Sexual orientation
- Substance use
{% endif %}
    """
    
    reading_level: Literal["simple", "general", "advanced"]
    allow_passive_voice: bool = False
    allow_split_inifitives: bool = False
    allow_wordiness: bool = False
    enforce_confidence: bool = True
    use_inclusive_gender: bool = True
    avoid_sensitive_topics: bool = True
    output_format: Literal["text", "markdown"] = "text"


# These will continue to evolve as issues arise
class WritingRules(TypedTemplate):
    engine: ClassVar[BaseTemplateEngine] = engine
    template_string: ClassVar[str] = """
## Writing Rules

{% if allow_acroynms %}
You may use acronyms in your writing.
{% if introduce_all_acroynms %}
When using an acronym for the first time, introduce it with its full form.
{% endif %}
{% else %}
Avoid using acronyms in your writing.
{% endif %}

{% if use_sentence_case_for_headings %}
Use sentence case for all headings (capitalize only the first word and proper nouns).
{% endif %}

{% if use_lowercase_for_email_and_urls %}
Use lowercase for email addresses and URLs.
{% endif %}

{% if no_all_caps_acronyms %}
Write acronyms in title case (e.g., Nasa) instead of all caps (e.g., NASA).
{% endif %}
    """

    allow_acroynms: bool =True
    introduce_all_acroynms: bool = True
    use_sentence_case_for_headings: bool = True
    use_lowercase_for_email_and_urls: bool = True
    no_all_caps_acronyms: bool = True

