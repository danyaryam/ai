def map_chat_to_features(user_input):
    message = user_input["message"].lower()

    # ===== DETECT =====
    if "tidak bisa tidur" in message or "insomnia" in message:
        sleep = "Poor"
    elif "tidur nyenyak" in message:
        sleep = "Good"
    else:
        sleep = "Average"

    if "cemas" in message or "stress" in message or "overthinking" in message:
        stress = "Often"
    else:
        stress = "Rarely"

    # ===== MAPPING KE DATASET =====
    return {
        "Age": user_input["age"],
        "Gender": user_input["gender"],
        "Country": "Indonesia",
        "self_employed": "No",
        "family_history": user_input["family_history"],
        "work_interfere": stress,  # 🔥 penting
        "no_employees": "1-5",
        "remote_work": "No",
        "tech_company": "Yes",
        "benefits": "No",
        "care_options": "No",
        "wellness_program": "No",
        "seek_help": "No",
        "anonymity": "Yes",
        "leave": "Somewhat difficult",
        "mental_health_consequence": "Yes" if stress == "Often" else "No",
        "phys_health_consequence": "No",
        "coworkers": "Some of them",
        "supervisor": "Some of them",
        "mental_health_interview": "No",
        "phys_health_interview": "No",
        "mental_vs_physical": "Don't know",
        "obs_consequence": "No"
    }