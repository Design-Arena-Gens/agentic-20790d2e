from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    Image,
    ListFlowable,
    ListItem,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
)


ROOT = Path(__file__).parent
OUTPUT_PDF = ROOT / "deliverables" / "php_tasks_report.pdf"


def build_document():
    OUTPUT_PDF.parent.mkdir(parents=True, exist_ok=True)

    doc = SimpleDocTemplate(
        str(OUTPUT_PDF),
        pagesize=A4,
        rightMargin=0.75 * inch,
        leftMargin=0.75 * inch,
        topMargin=0.75 * inch,
        bottomMargin=0.75 * inch,
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "Title",
        parent=styles["Title"],
        alignment=TA_CENTER,
        fontSize=32,
        leading=38,
        spaceAfter=24,
    )
    subtitle_style = ParagraphStyle(
        "Subtitle",
        parent=styles["Normal"],
        alignment=TA_CENTER,
        fontSize=16,
        leading=22,
        textColor=colors.HexColor("#444444"),
        spaceAfter=12,
    )
    heading_style = ParagraphStyle(
        "Heading",
        parent=styles["Heading2"],
        fontSize=18,
        leading=22,
        spaceAfter=6,
    )
    subheading_style = ParagraphStyle(
        "Subheading",
        parent=styles["Heading3"],
        fontSize=14,
        leading=18,
        textColor=colors.HexColor("#2A4365"),
        spaceBefore=12,
        spaceAfter=6,
    )
    body_style = ParagraphStyle(
        "Body",
        parent=styles["BodyText"],
        fontSize=11,
        leading=16,
        spaceAfter=6,
    )
    code_style = ParagraphStyle(
        "Code",
        parent=styles["Code"],
        fontName="Courier",
        fontSize=10,
        leading=13,
        backColor=colors.HexColor("#F5F5F5"),
        borderPadding=(8, 6, 8, 6),
        borderWidth=0.5,
        borderColor=colors.HexColor("#CCCCCC"),
        spaceBefore=8,
        spaceAfter=12,
    )

    story = []

    story.append(Spacer(1, 1.5 * inch))
    story.append(Paragraph("PHP Programming Tasks Report", title_style))
    story.append(
        Paragraph(
            "Nested Conditional Logic & String Manipulation Exercises",
            subtitle_style,
        )
    )
    story.append(Paragraph("Prepared by: Automated Codex Agent", subtitle_style))
    story.append(Spacer(1, 2 * inch))
    story.append(
        Paragraph(
            "This document presents two PHP programming tasks, detailing their aims, "
            "problem statements, constraints, procedures, implementations, sample outputs, "
            "and conclusions.",
            ParagraphStyle(
                "FrontBody",
                parent=body_style,
                alignment=TA_CENTER,
                leftIndent=36,
                rightIndent=36,
            ),
        )
    )
    story.append(PageBreak())

    tasks = [
        {
            "name": "Task 1: Largest of Three Numbers Using Nested If",
            "aim": "Determine the largest value among three given integers using nested conditional statements.",
            "problem": (
                "Build a PHP CLI program that accepts three predefined integers and "
                "evaluates them through nested if statements to identify the maximum."
            ),
            "constraints": [
                "The logic must rely on nested if statements rather than built-in max functions.",
                "The program should clearly display the input numbers and the computed largest number.",
            ],
            "procedure": [
                "Define an array containing three integer values.",
                "Assign the first value to a variable representing the current largest number.",
                "Compare the current largest with the second number using a nested if block and update when needed.",
                "Within the appropriate branches, compare against the third number to ensure the final value is the maximum.",
                "Print both the initial numbers and the final result for verification.",
            ],
            "program_path": ROOT / "code" / "task1_largest.php",
            "output_image": ROOT / "outputs" / "task1_output.png",
            "conclusion": (
                "Nested conditionals accurately identified the largest integer, "
                "demonstrating correct control flow for comparative evaluation."
            ),
        },
        {
            "name": "Task 2: Reverse a String Using strrev()",
            "aim": "Reverse a predefined string using PHP's built-in strrev function.",
            "problem": (
                "Create a PHP CLI script that stores a phrase in a string variable, applies "
                "strrev() to reverse it, and prints both the original and reversed outputs."
            ),
            "constraints": [
                "The solution must use the strrev() function to handle string reversal.",
                "Program output needs to highlight both the original string and its reversed counterpart clearly.",
            ],
            "procedure": [
                "Declare a string variable with the phrase targeted for reversal.",
                "Invoke PHP's strrev() function and store the reversed value.",
                "Display the original and reversed strings on separate lines for readability.",
            ],
            "program_path": ROOT / "code" / "task2_reverse.php",
            "output_image": ROOT / "outputs" / "task2_output.png",
            "conclusion": (
                "The strrev() function reversed the input phrase precisely, confirming "
                "the utility of PHP's standard library for string manipulation."
            ),
        },
    ]

    for index, task in enumerate(tasks):
        story.append(Paragraph(task["name"], heading_style))

        story.append(Paragraph("AIM", subheading_style))
        story.append(Paragraph(task["aim"], body_style))

        story.append(Paragraph("Problem Statement", subheading_style))
        story.append(Paragraph(task["problem"], body_style))

        story.append(Paragraph("Constraints", subheading_style))
        story.append(
            ListFlowable(
                [ListItem(Paragraph(item, body_style)) for item in task["constraints"]],
                bulletType="bullet",
                start="bullet",
                bulletFontSize=10,
            )
        )

        story.append(Paragraph("Procedure", subheading_style))
        story.append(
            ListFlowable(
                [ListItem(Paragraph(step, body_style)) for step in task["procedure"]],
                bulletType="1",
                start="1",
                bulletFontSize=10,
            )
        )

        story.append(Paragraph("Program", subheading_style))
        code_text = task["program_path"].read_text().strip().replace("\n", "<br/>")
        story.append(Paragraph(code_text, code_style))

        story.append(Paragraph("Output", subheading_style))
        story.append(
            Paragraph(
                "Screenshot of the CLI output captured after executing the PHP script:",
                body_style,
            )
        )
        output_img = Image(str(task["output_image"]))
        output_img._restrictSize(5.5 * inch, 3.5 * inch)
        story.append(output_img)

        story.append(Paragraph("Conclusion", subheading_style))
        story.append(Paragraph(task["conclusion"], body_style))

        if index != len(tasks) - 1:
            story.append(PageBreak())

    doc.build(story)


if __name__ == "__main__":
    build_document()
