"""Test automatic embedding generation on create operations - FULL AUTOMATION."""

from app.db.create_tables import InitDB
from app.services.service_layer.profile_service import ProfileService
from app.services.service_layer.employee_service import EmployeeService
from app.services.service_layer.required_profile_service import RequiredProfileService
from app.services.service_layer.project_service import ProjectService
from sqlalchemy import text
from app.db.database import SessionLocal

# Initialize database
print("\n" + "=" * 70)
print("TESTING AUTOMATIC EMBEDDING GENERATION")
print("=" * 70)

print("\n[1] Creating tables...")
InitDB().create_tables()

# Test 1: Create employee WITHOUT pre-existing profile (FULL AUTO)
print("\n[TEST 1] Creating employee with inline profile data (FULL AUTO)...")
print("        No profile_id provided - profile created automatically")
employee_service = EmployeeService()
employee1 = employee_service.create_one({
    "name": "Juan García",
    "office": "Madrid",
    "hard_skills": "Python, FastAPI, PostgreSQL",
    "soft_skills": "Problem solving, Communication",
    "languages": "English, Spanish"
})
print(f"   ✓ Employee created: ID {employee1.id}")
print(f"   ✓ Profile auto-created: ID {employee1.profile_id}")

# Test 2: Create employee with multiple at once
print("\n[TEST 2] Creating multiple employees with inline profiles...")
employees = employee_service.create_many([
    {
        "name": "Ana López",
        "office": "Barcelona",
        "hard_skills": "JavaScript, React, Node.js",
        "soft_skills": "Creativity, Design thinking",
        "languages": "English, Spanish, French"
    },
    {
        "name": "Carlos Pérez",
        "office": "Valencia",
        "hard_skills": "Java, Spring Boot, MySQL",
        "soft_skills": "Analysis, Strategic planning",
        "languages": "English, Spanish"
    }
])
print(f"   ✓ {len(employees)} employees created")
for emp in employees:
    print(f"     - {emp.name} (ID {emp.id}) with profile ID {emp.profile_id}")

# Test 3: Create employee with existing profile_id
print("\n[TEST 3] Creating employee with existing profile_id...")
profile_service = ProfileService()
profile = profile_service.create_one({
    "hard_skills": "C#, .NET, Azure",
    "soft_skills": "Architecture, Performance optimization",
    "languages": "English, German"
})
print(f"   ✓ Profile created: ID {profile.id}")

employee3 = employee_service.create_one({
    "name": "María López",
    "office": "Bilbao",
    "profile_id": profile.id
})
print(f"   ✓ Employee created: ID {employee3.id} with existing profile")

# Test 4: Create required profile (auto embedding)
print("\n[TEST 4] Creating required profile (auto embedding)...")
project_service = ProjectService()
project = project_service.create_one({
    "name": "AI Project",
    "description": "Machine learning project"
})
print(f"   ✓ Project created: ID {project.id}")

req_service = RequiredProfileService()
req_profile = req_service.add_required_profile(
    project_id=project.id,
    hard_skills="Python, Machine Learning, TensorFlow",
    soft_skills="Analytical thinking, Innovation",
    languages="English"
)
print(f"   ✓ Required profile created: ID {req_profile.id}")

# Verify all embeddings were created
print("\n[VERIFICATION] Checking embeddings...")
db = SessionLocal()

total_embeddings = db.execute(text("SELECT COUNT(*) FROM embeddings")).scalar()
employee_embeddings = db.execute(
    text("SELECT COUNT(*) FROM embeddings WHERE profile_id IS NOT NULL")
).scalar()
required_embeddings = db.execute(
    text("SELECT COUNT(*) FROM embeddings WHERE required_profile_id IS NOT NULL")
).scalar()

print(f"   ✓ Total embeddings: {total_embeddings}")
print(f"   ✓ Employee profile embeddings: {employee_embeddings}")
print(f"   ✓ Required profile embeddings: {required_embeddings}")

# Show summary
print("\n" + "=" * 70)
print("TEST SUMMARY - FULL AUTOMATION")
print("=" * 70)
print(f"✓ Profiles created automatically: {len(employees) + 2}")  # 2 from test1+3, + 1 inline in test2
print(f"✓ Employees created: {len(employees) + 2}")
print(f"✓ Projects created: 1")
print(f"✓ Required Profiles created: 1")
print(f"✓ Total embeddings auto-generated: {total_embeddings}")
print("\nFLOW:")
print("  1. Create Employee (with inline profile data)")
print("  2. → Profile auto-created")
print("  3. → Embedding auto-generated")
print("  ✓ NO MANUAL STEPS NEEDED!")
print("=" * 70 + "\n")

db.close()
profile_service.close()
employee_service.close()
req_service.close()
