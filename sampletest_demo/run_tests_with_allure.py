import subprocess
import os

def run_tests_and_generate_allure():
    project_dir = "/Users/narendraiyer/MyProjects/MyDocs/sampletest_demo"
    allure_results = os.path.join(project_dir, "allure-results")
    allure_report = os.path.join(project_dir, "allure-report")

    # Run pytest with Allure
    subprocess.run([
        "pytest",
        "--alluredir", allure_results
    ], cwd=project_dir)

    # Generate Allure Report
    subprocess.run([
        "allure",
        "generate", allure_results,
        "-o", allure_report,
        "--clean"
    ], cwd=project_dir)

    # Open the report in browser
    subprocess.run([
        "allure",
        "open", allure_report
    ], cwd=project_dir)

if __name__ == "__main__":
    run_tests_and_generate_allure()

