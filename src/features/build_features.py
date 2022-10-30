from json import load

# reading the json file into the data list
with open("data/maestro_sample_log.json") as jsonfile:
    data = load(jsonfile)
jsonfile.close()

processed = []
for i in data:
    sample = data[i]
    name = sample['name']
    storage_slot = sample['storage_slot']['slot']
    storage_tray = sample['storage_slot']['tray']
    substrate = sample['substrate']
    worklist = sample['worklist'] # where all the steps happen
    hotplate = sample['hotplate_slot']['hotplate']
    hoteplate_slot = sample['hotplate_slot']['slot']
    processed.append([name, storage_slot, storage_tray, substrate, worklist, hotplate, hoteplate_slot])

def flatten_characterization(worklist):
    result = {}
    for task in worklist:
        if 'details' in task and 'characterization_tasks' in task['details']:
            for image_type in task['details']['characterization_tasks']:
                img_station =  image_type['station']
                if 'exposure_times' in image_type['details']:
                    result['{}_exposure_time'.format(img_station)] = image_type['details']['exposure_times']
                elif 'exposure_time' in image_type['details']:
                    result['{}_exposure_time'.format(img_station)] = image_type['details']['exposure_time']
                if 'num_scans' in image_type['details']:
                    result['{}_num_scan'.format(img_station)] = image_type['details']['num_scans']
                elif 'num_scan' in image_type['details']:
                    result['{}_num_scan'.format(img_station)] = image_type['details']['num_scan']
                result['{}_duration'.format(img_station)] = image_type['duration']
        #         result['{}_name'.format(img_station)] = task['name']
                result['{}_position'.format(img_station)] = image_type['position']
    return result

def flatten_drops(worklist):
    """ does not work as intended at the moment
    sample0 has 2 drops step on step 7"""
    result = {}
    i = 1
    for task in worklist:
        if 'details' in task and 'drops' in task['details']:
            for drop_task in task['details']['drops']:
                result['drop{}_air_gap'.format(i)] = drop_task['air_gap']
                result['drop{}_blow_out'.format(i)] = drop_task['blow_out']
                result['drop{}_height'.format(i)] = drop_task['height']
                result['drop{}_pre_mix'.format(i)] = drop_task['pre_mix']
                result['drop{}_rate'.format(i)] = drop_task['rate']
                result['drop{}_reuse_tip'.format(i)] = drop_task['reuse_tip']
                result['drop{}_slow_retract'.format(i)] = drop_task['slow_retract']
                result['drop{}_slow_travel'.format(i)] = drop_task['slow_travel']
#                 result['drop{}_solution'.format(i)] = task['solution']
                result['drop{}_solution_molarity'.format(i)] = drop_task['solution']['molarity']
                result['drop{}_solution_solutes'.format(i)] = drop_task['solution']['solutes']
                result['drop{}_solution_solvent'.format(i)] = drop_task['solution']['solvent']
                result['drop{}_solution_well_labware'.format(i)] = drop_task['solution']['well']['labware']
                result['drop{}_solution_well'.format(i)] = drop_task['solution']['well']['well']
                result['drop{}_time'.format(i)] = drop_task['time']
                result['drop{}_touch_tip'.format(i)] = drop_task['touch_tip']
                result['drop{}_volume'.format(i)] = drop_task['volume']

            result['drop{}_start_times'.format(i)] = task['details']['start_times']
            result['drop{}_duration'.format(i)] = task['details']['duration']
            result['drop{}_steps'.format(i)] = task['details']['steps']
                
            result['drop{}_id'.format(i)] = task['id']
            result['drop{}_name'.format(i)] = task['name']
            result['drop{}_precedent'.format(i)] = task['precedent']
            result['drop{}_sample'.format(i)] = task['sample']
            result['drop{}_start'.format(i)] = task['start']
            result['drop{}_start_actual'.format(i)] = task['start_actual']
            result['drop{}_liquidhandler_timings'.format(i)] = task['liquidhandler_timings']
            result['drop{}_spincoater_log'.format(i)] = task['spincoater_log']
            result['drop{}_headstart'.format(i)] = task['headstart']
            result['drop{}_finish_actual'.format(i)] = task['finish_actual']
            i += 1
    return result