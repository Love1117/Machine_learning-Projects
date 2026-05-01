def encode_bp(bp_status):
        return {"bp_Hypertension Stage 1": 1 if bp_status == "stage1" else 0,
                "bp_Hypertension Stage 2": 1 if bp_status == "stage2" else 0,
                "bp_Normal": 1 if bp_status == "normal" else 0,}
