from django.shortcuts import render
from one_step_frames.step_frame_conditions import findStepFrameCondition

def to_latex(formula: str) -> str:
    latex = formula

    # quantifiers
    latex = latex.replace("F", r"\forall ")
    latex = latex.replace("E", r"\exists ")

    # logical connectives
    latex = latex.replace("->", r"\to ")
    latex = latex.replace("<->", r"\leftrightarrow ")
    latex = latex.replace("&", r"\land ")
    latex = latex.replace("|", r"\lor ")
    latex = latex.replace("~", r"\neg ")

    # equality / relations
    latex = latex.replace("!=", r"\neq ")
    latex = latex.replace("?", r"\subseteq ")
    latex = latex.replace("∈", r"\in ")

    return latex


def home(request):
    output = ""
    rendered_formula = None

    if request.method == "POST":
        rule = request.POST.get("user_input", "")
        translated = findStepFrameCondition(rule)

        if translated:
            rendered_formula = to_latex(translated)

        output = f"{rendered_formula}"

    return render(request, "home.html", {"output": output})
