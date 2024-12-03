# dummy draft code for hack week
# License compatibility matrix
COMPATIBILITY_MATRIX = {
    ("MIT", "GPL-3.0"): True,
    ("GPL-3.0", "MIT"): False,
    ("Apache-2.0", "GPL-3.0"): True,
    ("Proprietary", "GPL-3.0"): False
}

# Function to check license compatibility
def is_compatible(project_license, dependency_license):
    return COMPATIBILITY_MATRIX.get((project_license, dependency_license), False)

# Main algorithm
def check_license_compatibility(project_licenses, dependencies):
    report = {"compatible": True, "issues": []}
    
    for dependency in dependencies:
        dep_name = dependency["name"]
        dep_license = dependency["license"]
        compatible_with_all = True
        
        for proj_license in project_licenses:
            if not is_compatible(proj_license, dep_license):
                compatible_with_all = False
                report["issues"].append({
                    "dependency": dep_name,
                    "license": dep_license,
                    "reason": f"{dep_license} is incompatible with {proj_license}"
                })
        
        if not compatible_with_all:
            report["compatible"] = False

    return report

# Example input
project_licenses = ["GPL-3.0"]
dependencies = [
    {"name": "dependency1", "license": "Apache-2.0"},
    {"name": "dependency2", "license": "MIT"},
    {"name": "dependency3", "license": "Proprietary"}
]

# Run the algorithm
result = check_license_compatibility(project_licenses, dependencies)

# Print results
if result["compatible"]:
    print("All licenses are compatible!")
else:
    print("License compatibility issues found:")
    for issue in result["issues"]:
        print(f"- {issue['dependency']} ({issue['license']}): {issue['reason']}")
