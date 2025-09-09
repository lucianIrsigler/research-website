from django.shortcuts import render
from one_step_frames.step_frame_conditions import findStepFrameCondition, getLogs

def to_latex(formula: str) -> str: 
    latex = formula
    latex = latex.replace("F", r"\forall ") 
    latex = latex.replace("E", r"\exists ") 
    latex = latex.replace("->", r"\to ") 
    latex = latex.replace("<->", r"\leftrightarrow ") 
    latex = latex.replace("&", r"\land ") 
    latex = latex.replace("|", r"\lor ") 
    latex = latex.replace("~", r"\neg ") 
    latex = latex.replace("!=", r"\neq ") 
    latex = latex.replace("?", r"\subseteq ") 
    latex = latex.replace("∈", r"\in ") 
    return latex

def home(request):
    output = ""
    logs_text = ""
    solution_text = ""
    
    if request.method == "POST":
        rule = request.POST.get("user_input", "")
        logs = None
        output = None

        try:
            logs = getLogs(rule)
            output = findStepFrameCondition(rule)
        except Exception as e:
            print(e)
        
        if (output==None or logs==None):
            return render(request, "home.html", {
                "output": "",
                "logs_text": [],
                "solution_text": "",
                "user_input": request.POST.get("user_input", "")
            })
        
        output = to_latex(output)
        # Prepare log strings
        if logs and len(logs) > 0:
            logs_text = "\n".join(logs[0]) if logs[0] else "No logs yet..."
            solution_text = "\n".join(f"{k}: {v}" for k, v in logs[1].items()) if len(logs) > 1 else "No solution yet..."
    
    return render(request, "home.html", {
        "output": output,
        "logs_text": logs_text,
        "solution_text": solution_text,
        "user_input": request.POST.get("user_input", "")
    })
