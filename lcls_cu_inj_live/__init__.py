from lcls_cu_inj_live.files import VARIABLE_FILE
from lume_model.utils import variables_from_yaml

INPUT_VARIABLES, OUTPUT_VARIABLES = variables_from_yaml(VARIABLE_FILE)
