rule data_gen:
    output: "src/data/red_data.tar.gz"
    input: 
        "src/data/data.tar.gz"
    cache: True
    script: "src/scripts/red_data_gen.py"