# Marksmanship.py
import xml.etree.ElementTree as ET
from Util import process_file

BASE_PERCENTAGES = [0.04, 0.07, 0.11, 0.16]
NEW_PERCENTAGES = [0.05, 0.1, 0.15, 0.2]

MARKSMANSHIP_TYPES = {
    'PlasmaRifleMarksmanship': BASE_PERCENTAGES,
    'DMRMarksmanship': BASE_PERCENTAGES,
    'MachinegunMarksmanship': BASE_PERCENTAGES,
    'MinigunMarksmanship': BASE_PERCENTAGES,
    'RifleMarksmanship': BASE_PERCENTAGES,
    'ShotgunMarksmanship': BASE_PERCENTAGES,
    'Tactics': [BASE_PERCENTAGES[0], None, BASE_PERCENTAGES[1], None]
}

def modify_marksmanship(xml_file_path):
    # Parse the XML file
    tree = ET.parse(xml_file_path)
    root = tree.getroot()

    # Iterate through each weapon  marks type
    for weapon_type, marksmanship_types in MARKSMANSHIP_TYPES.items():
        # Iterate through each marks level for each weapon
        for i, type in enumerate(marksmanship_types):
            if type is not None and (effect_nodes := root.findall(f'.//CUpgrade[@id="{weapon_type}{i + 1}"]/EffectArray')):
                current_weapon = f"{weapon_type}{i + 1}"
                print(f"\nProcessing weapon: {current_weapon}")

                percentage_index = i
                #Special Case Tactics Level 3
                if current_weapon == 'Tactics3':
                    percentage_index = 1

                for effect_node in effect_nodes:
                    reference = effect_node.get('Reference')
                    value_str = effect_node.get('Value')

                    # Check if the value is a valid float
                    try:
                        amount = float(value_str)
                    except ValueError:
                        # Handle the case where the value is not a valid float
                        print(f"Skipping EffectArray: {reference}, Invalid Value: {value_str}")
                        continue

                    print(f"Checking EffectArray: {reference}, Current Value: {amount}")

                    # Check if the reference contains "Amount" or "Random"
                    if 'Amount' in reference or 'Random' in reference:
                        # Calculate new percentage
                        modified_amount = (amount / type) * NEW_PERCENTAGES[percentage_index]

                        # Update the XML with the modified value
                        effect_node.set('Value', str(round(modified_amount, 2)))

                        # Debug amount change
                        print(f"Changed {reference} to {round(modified_amount, 2)}")

    # Convert to string and format for sc2
    xml_string = ET.tostring(root, encoding='unicode')
    xml_declaration = '<?xml version="1.0" encoding="utf-8"?>\n'
    xml_string = xml_declaration + xml_string
    xml_string = xml_string.replace(" />", "/>")

    # Save xml file
    with open(xml_file_path, "w", encoding='utf-8') as xml_file:
        xml_file.write(xml_string)

#Update tooltips
def modify_txt_file(txt_file_path, new_percentages):
    # Read the contents of the file
    with open(txt_file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Modify the lines containing the specific keys
    for i in range(len(lines)):
        original_line = lines[i]  # Store the original line for debugging
        if 'UI/CampaignPurchase/InfoDialog/UAD/Standard/Item1/Description' in lines[i]:
            lines[i] = f'UI/CampaignPurchase/InfoDialog/UAD/Standard/Item1/Description={new_percentages[0]*100:.0f}%\n'
            print(f"Changed line from: {original_line.strip()} to: {lines[i].strip()}")
        elif 'UI/CampaignPurchase/InfoDialog/UAD/Standard/Item2/Description' in lines[i]:
            lines[i] = f'UI/CampaignPurchase/InfoDialog/UAD/Standard/Item2/Description={new_percentages[1]*100:.0f}%\n'
            print(f"Changed line from: {original_line.strip()} to: {lines[i].strip()}")
        elif 'UI/CampaignPurchase/InfoDialog/UAD/Standard/Item3/Description' in lines[i]:
            lines[i] = f'UI/CampaignPurchase/InfoDialog/UAD/Standard/Item3/Description={new_percentages[2]*100:.0f}%\n'
            print(f"Changed line from: {original_line.strip()} to: {lines[i].strip()}")
        elif 'UI/CampaignPurchase/InfoDialog/UAD/Standard/Item1/Title' in lines[i]:
            lines[i] = f'UI/CampaignPurchase/InfoDialog/UAD/Standard/Item1/Title={new_percentages[3]*100:.0f}%\n'
            print(f"Changed line from: {original_line.strip()} to: {lines[i].strip()}")

    # save txt file
    with open(txt_file_path, 'w', encoding='utf-8') as file:
        file.writelines(lines)

def main():
    xml_relative_path = '../../Development/UA Data.SC2Mod/Base.SC2Data/GameData/UpgradeData.xml'
    process_file(xml_relative_path, "XML file", modify_marksmanship)

    txt_relative_path = '../../Development/UA Data.SC2Mod/enUS.SC2Data/LocalizedData/Gamestrings.txt'
    process_file(txt_relative_path, "Text file", modify_txt_file, NEW_PERCENTAGES)

if __name__ == "__main__":
    main()