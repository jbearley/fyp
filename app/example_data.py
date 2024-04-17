"""
FYP Table
{
	"semester_key_1": {
		"class_key_1": <class>,
		"class_key_2": <class>,
		"class_key_3": <class>,
		"class_key_4": <class>,
		"class_key_5": <class>,
	},
	...
}

Requirements Table (So that we can justify the FYP result on the front-end)
{
    "major_1": {
        "singles": [
            "class_key_1",
            "class_key_2",
            ...
        ],
        "pick_1_description1": [
            "class_key_3",
            "class_key_4",
            ...
        ],
        "pick_1_description2": [
            "class_key_5",
            "class_key_6",
            ...
        ],
        "pick_2_description3": [
            "class_key_7",
            "class_key_8",
            "class_key_9",
            "class_key_10",
            ...
        ],
    },
    "major_2": <major 2 requirements, similar to above>,
    "AOIs": <requirements, similarly indicating any pick-1s, etc.>,
    "total_credits": <min # of credits for graduation>
}
"""
