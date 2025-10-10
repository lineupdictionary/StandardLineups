import os
import json

def main():
    num_custom_lineups = 0
    root_dir = os.path.dirname(os.path.abspath(__file__))

    for dirpath, dirnames, filenames in os.walk(root_dir):
        if "Lineup.txt" in filenames:
            #success = True
            file_path = os.path.join(dirpath, "lineup.txt")
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                
                # Case 2: parsed successfully, but custom_lineup is explicitly false
                if isinstance(data, dict) and data.get("custom_lineup") is True:
                    print(f"Custom lineup → {file_path}")
                    #success = False
                    num_custom_lineups += 1

            except json.JSONDecodeError:
                # Case 1: JSON parsing failed
                print(f"WARNING: JSON parse error → {file_path}")
                #success = False
            except Exception as e:
                # Catch any unexpected error
                print(f"WARNING: Unexpected error ({e}) → {file_path}")
                #success = False


            #if success:
            #    print("Non custom lineup", file_path)
    print("Number of custom lineups found: ", num_custom_lineups)

if __name__ == "__main__":
    main()