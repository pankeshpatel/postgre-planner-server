

from config.db import Base
from sqlalchemy import Column,  String, Integer

class User(Base):
    __tablename__ = 'User'
    
    id = Column(String(45), primary_key=True, index=True)
    username = Column('username', String(45))
    password = Column( 'password', String(255))  
    

class ExceptionMessage(Base):
    __tablename__ = "ExceptionMessage"
    
    id = Column(String(45), primary_key=True, index=True)
    exceptionID = Column('exceptionID', Integer)
    message  =  Column('message', String(225))
    
class Planner(Base):
    __tablename__ = "Planner"
    
    planner_id =  Column(Integer, primary_key=True, autoincrement=True)
    id = Column('id', String(225))
    name = Column('name', String(225))
    email = Column('email', String(225))   

class MaterialMaster(Base):
    __tablename__ = "MaterialMaster"
    
    id = Column(String(45), primary_key=True, index=True)
    initial_creation_date = Column('initial_creation_date', String(225))	
    last_change_date = Column('last_change_date', String(225))	
    material = Column('material', String(225))	
    material_9 = Column('material_9', String(225))	
    material_7 = Column('material_7', String(225))
    ai = Column('ai', String(225))	
    mat_description = Column('mat_description', String(225))	
    mat_description_eng = Column('mat_description_eng', String(225))	
    plant = Column('plant', String(225))	
    planner = Column('planner', String(225))	
    replenishment_type = Column('replenishment_type', String(225))	
    rounding_value = Column('rounding_value', String(225))	
    lot_size = Column('lot_size', String(225))	
    minimum_lot_size = Column('minimum_lot_size', String(225))
    safety_time_days= Column('safety_time_days', String(225))	
    safety_time_ind = Column('safety_time_ind', String(225))	
    leadtime_hours = Column('leadtime_hours', String(225))
    planning_time_fence = Column('planning_time_fence', String(225))	
    planned_delivery_time = Column('planned_delivery_time', String(225))	
    safety_stock = Column('safety_stock', String(225))	
    unit_of_quantity = Column('unit_of_quantity', String(225))
    length = Column('length', String(225))	
    width = Column('width', String(225))	
    height = Column('height', String(225))
    uom_lwh = Column('uom_lwh', String(225))	
    volume = Column('volume', String(225))
    unit_of_volume = Column('unit_of_volume', String(225))	
    gross_weight = Column('gross_weight', String(225))	
    net_weight = Column('net_weight', String(225))	
    unit_of_weight = Column('unit_of_weight', String(225))
    stacking_factor = Column('stacking_factor', String(225))	
    material_group = Column('material_group', String(225))
    run_out_date = Column('run_out_date', String(225))
    proc_type = Column('proc_type', String(225))	
    part_type = Column('part_type', String(225))	
    character = Column('character', String(225))	
    init_upg = Column('init_upg', String(225))
    init_use_type= Column('init_use_type', String(225))	
    procurement_type = Column('procurement_type', String(225))	
    storage_location = Column('storage_location', String(225))	
    bwd_consumption_per = Column('bwd_consumption_per', String(225))	
    fwd_consumption_per = Column('fwd_consumption_per', String(225))	
    pps_planning_calendar = Column('pps_planning_calendar', String(225))	
    factory_calendar = Column('factory_calendar', String(225))	
    mrp_group = Column('mrp_group', String(225))	
    mixed_mrp = Column('mixed_mrp', String(225))	
    strategy_group = Column('strategy_group', String(225))	
    consumption_mode = Column('consumption_mode', String(225))
    abc_indicator = Column('abc_indicator', String(225))
    spab_indicator = Column('spab_indicator', String(225))	
    status = Column('status', String(225))
    status_valid_from = Column('status_valid_from', String(225))	
    bulk_material = Column('bulk_material', String(225))	
    omb_part = Column('omb_part', String(225))
    warehouse_number = Column('warehouse_number', String(225))
    storage_type_stock_placement = Column('storage_type_stock_placement', String(225))
    storage_type_stock_removement = Column('storage_type_stock_removement', String(225))	
    release = Column('release', String(225))	
    release_date = Column('release_date', String(225))
    release_type = Column('release_type', String(225))	
    release_action_code = Column('release_action_code', String(225))	
    active_material = Column('active_material', String(225))	
    plant_calendar = Column('plant_calendar', String(225))
    document_number = Column('document_number', String(225))	
    sid_client = Column('sid_client', String(225))
    snapdate = Column('snapdate', String(225))
    snaptimestamp = Column('snaptimestamp', String(225))	
    load_date = Column('load_date', String(225))	
    load_timestamp = Column('load_timestamp', String(225))	
    _load_date = Column('_load_date', String(225))
    
class Exception(Base):
    __tablename__ = "Exception"
    
    id = Column(String(45), primary_key=True, index=True)
    mandt = Column('mandt', String(225))
    matnr = Column('matnr', String(225))
    aline = Column('aline', String(225))
    cdate = Column('cdate', String(225))
    ctime = Column('ctime', String(225))
    dat00 = Column('dat00', String(225))
    delb0 = Column('delb0', String(225))
    extra = Column('extra', String(225))
    umdat = Column('umdat', String(225))
    auskt = Column('auskt', Integer)
    mng01 = Column('mng01', String(225))
    mng02 = Column('mng02', String(225))
    p_ingestday = Column('p_ingestday', String(225))
    p_ingesttime = Column('p_ingesttime', String(225))
    
    
class MD04(Base):
    __tablename__ = "MD04"
    
    id = Column(String(45), primary_key=True, index=True)
    material = Column("material", String(225))
    plant = Column("plant", String(225))
    mrp_area = Column("mrp_area", String(225))
    demand_date = Column("demand_date", String(225))
    mrp_element_cd = Column("mrp_element_cd", String(225))
    shipping_notification = Column("shipping_notification", String(225))
    container_info = Column("container_info", String(225))
    mrp_element = Column("mrp_element", String(225))
    change_quantity = Column("change_quantity", Integer)
    total_quantity = Column("total_quantity", Integer)
    storage_location = Column("storage_location", String(225))
    supplier_nr = Column("supplier_nr", String(225))
    planner = Column("planner", String(225))
    split_indicator = Column("split_indicator", String(225))
    line_index = Column("line_index", String(225))
    document_uuid = Column("document_uuid", String(225))
    sid_client = Column("sid_client", String(225))
    snapdate = Column("snapdate", String(225))
    snaptime = Column("snaptime", String(225))
    load_date = Column("load_date", String(225))
    load_timestamp = Column("load_timestamp", String(225))
    _load_date = Column("_load_date", String(225))
    
class Zgrve(Base):
    __tablename__ = "Zgrve"
    
    id = Column(String(45), primary_key=True, index=True)
    mandt = Column("mandt", String(225))
    lifnr = Column("lifnr", String(225))
    delnote = Column("delnote", String(225))
    trailer = Column("trailer", String(225))
    matnr = Column("matnr", String(225))
    mblnr = Column("mblnr", String(225))
    itmno = Column("itmno", String(225))
    erdat = Column("erdat", String(225))
    erfmg = Column("erfmg", String(225))
    meins = Column("meins", String(225))
    ebeln = Column("ebeln", String(225))
    ebelp = Column("ebelp", String(225))
    werks = Column("werks", String(225))
    lgort = Column("lgort", String(225))
    bwart = Column("bwart", String(225))
    rct_ident = Column("rct_ident", String(225))
    crttime = Column("crttime", String(225))
    status = Column("status", String(225))
    shkzg = Column("shkzg", String(225))
    vbeln =  Column("vbeln", String(225))
    bolnr = Column("bolnr", String(225))
    p_ingestday = Column("p_ingestday", String(225))
    p_ingesttime = Column("p_ingesttime", String(225))



# dbZgrve = Table(
#         "Zgrve",
#         meta,
#         Column("mandt", String(225)),
#         Column("lifnr", String(225)),
#         Column("delnote", String(225)),
#         Column("trailer", String(225)),
#         Column("matnr", String(225)),
#         Column("mblnr", String(225)),
#         Column("itmno", String(225)),
#         Column("erdat", String(225)),
#         Column("erfmg", String(225)),
#         Column("meins", String(225)),
#         Column("ebeln", String(225)),
#         Column("ebelp", String(225)),
#         Column("werks", String(225)),
#         Column("lgort", String(225)),
#         Column("bwart", String(225)),
#         Column("rct_ident", String(225)),
#         Column("crttime", String(225)),
#         Column("status", String(225)),
#         Column("shkzg", String(225)),
#         Column("vbeln", String(225)),
#         Column("bolnr", String(225)),
#         Column("p_ingestday", String(225)),
#         Column("p_ingesttime", String(225))
# )

    
# dbmd04 = Table(
#             "MD04",
#             meta,
#             Column("material", String(225)),
#             Column("plant", String(225)),
#             Column("mrp_area", String(225)),
#             Column("demand_date", String(225)),
#             Column("mrp_element_cd", String(225)),
#             Column("shipping_notification", String(225)),
#             Column("container_info", String(225)),
#             Column("mrp_element", String(225)),
#             Column("change_quantity", Integer),
#             Column("total_quantity", Integer),
#             Column("storage_location", String(225)),
#             Column("supplier_nr", String(225)),
#             Column("planner", String(225)),
#             Column("split_indicator", String(225)),
#             Column("line_index", String(225)),
#             Column("document_uuid", String(225)),
#             Column("sid_client", String(225)),
#             Column("snapdate", String(225)),
#             Column("snaptime", String(225)),
#             Column("load_date", String(225)),
#             Column("load_timestamp", String(225)),
#             Column("_load_date", String(225))
#     )


# dbExceptionManager = Table (
#                     "Exception", 
#                     meta,
#                     Column('mandt', String(225)),
#                     Column('matnr', String(225)),
#                     Column('aline', String(225)),
#                     Column('cdate', String(225)),
#                     Column('ctime', String(225)),
#                     Column('dat00', String(225)),
#                     Column('delb0', String(225)),
#                     Column('extra', String(225)),
#                     Column('umdat', String(225)),
#                     Column('auskt', Integer),
#                     Column('mng01', String(225)),
#                     Column('mng02', String(225)),
#                     Column('p_ingestday', String(225)),
#                     Column('p_ingesttime', String(225))
# 				)


# dbMaterialMaster = Table (
#                     "MaterialMaster", 
#                     meta,
# Column('initial_creation_date', String(225)),	
# Column('last_change_date', String(225)),	
# Column('material', String(225)),	
# Column('material_9', String(225)),	
# Column('material_7', String(225)),	
# Column('ai', String(225)),	
# Column('mat_description', String(225)),	
# Column('mat_description_eng', String(225)),	
# Column('plant', String(225)),	
# Column('planner', String(225)),	
# Column('replenishment_type', String(225)),	
# Column('rounding_value', String(225)),	
# Column('lot_size', String(225)),	
# Column('minimum_lot_size', String(225)),	
# Column('safety_time_days', String(225)),	
# Column('safety_time_ind', String(225)),	
# Column('leadtime_hours', String(225)),	
# Column('planning_time_fence', String(225)),	
# Column('planned_delivery_time', String(225)),	
# Column('safety_stock', String(225)),	
# Column('unit_of_quantity', String(225)),	
# Column('length', String(225)),	
# Column('width', String(225)),	
# Column('height', String(225)),	
# Column('uom_lwh', String(225)),	
# Column('volume', String(225)),	
# Column('unit_of_volume', String(225)),	
# Column('gross_weight', String(225)),	
# Column('net_weight', String(225)),	
# Column('unit_of_weight', String(225)),	
# Column('stacking_factor', String(225)),	
# Column('material_group', String(225)),	
# Column('run_out_date', String(225)),	
# Column('proc_type', String(225)),	
# Column('part_type', String(225)),	
# Column('character', String(225)),	
# Column('init_upg', String(225)),	
# Column('init_use_type', String(225)),	
# Column('procurement_type', String(225)),	
# Column('storage_location', String(225)),	
# Column('bwd_consumption_per', String(225)),	
# Column('fwd_consumption_per', String(225)),	
# Column('pps_planning_calendar', String(225)),	
# Column('factory_calendar', String(225)),	
# Column('mrp_group', String(225)),	
# Column('mixed_mrp', String(225)),	
# Column('strategy_group', String(225)),	
# Column('consumption_mode', String(225)),	
# Column('abc_indicator', String(225)),	
# Column('spab_indicator', String(225)),	
# Column('status', String(225)),	
# Column('status_valid_from', String(225)),	
# Column('bulk_material', String(225)),	
# Column('omb_part', String(225)),	
# Column('warehouse_number', String(225)),	
# Column('storage_type_stock_placement', String(225)),	
# Column('storage_type_stock_removement', String(225)),	
# Column('release', String(225)),	
# Column('release_date', String(225)),	
# Column('release_type', String(225)),	
# Column('release_action_code', String(225)),	
# Column('active_material', String(225)),	
# Column('plant_calendar', String(225)),	
# Column('document_number', String(225)),	
# Column('sid_client', String(225)),	
# Column('snapdate', String(225)),	
# Column('snaptimestamp', String(225)),	
# Column('load_date', String(225)),	
# Column('load_timestamp', String(225)),	
# Column('_load_date', String(225))
# )   
  


# from sqlalchemy import Table, Column
# from sqlalchemy.sql.sqltypes import Integer, String, DateTime, Date
# from config.db import meta, engine


# dbUsers = Table(
#     'User',
#     meta,   
#     Column('username', String(45)),
#     Column('password', String(255))   
# )

# dbExceptionMessage = Table(
#                     "ExceptionMessage", 
#                     meta, 
#                     Column('exceptionID', Integer),
#                     Column('message', String(225))                
#                 )

# dbPlanner = Table(
#                     "Planner", 
#                     meta, 
#                     Column('id', String(225)),
#                     Column('name', String(225)),
#                     Column('email', String(225))              
#                 )



# dbMaterialMaster = Table (
#                     "MaterialMaster", 
#                     meta,
# Column('initial_creation_date', String(225)),	
# Column('last_change_date', String(225)),	
# Column('material', String(225)),	
# Column('material_9', String(225)),	
# Column('material_7', String(225)),	
# Column('ai', String(225)),	
# Column('mat_description', String(225)),	
# Column('mat_description_eng', String(225)),	
# Column('plant', String(225)),	
# Column('planner', String(225)),	
# Column('replenishment_type', String(225)),	
# Column('rounding_value', String(225)),	
# Column('lot_size', String(225)),	
# Column('minimum_lot_size', String(225)),	
# Column('safety_time_days', String(225)),	
# Column('safety_time_ind', String(225)),	
# Column('leadtime_hours', String(225)),	
# Column('planning_time_fence', String(225)),	
# Column('planned_delivery_time', String(225)),	
# Column('safety_stock', String(225)),	
# Column('unit_of_quantity', String(225)),	
# Column('length', String(225)),	
# Column('width', String(225)),	
# Column('height', String(225)),	
# Column('uom_lwh', String(225)),	
# Column('volume', String(225)),	
# Column('unit_of_volume', String(225)),	
# Column('gross_weight', String(225)),	
# Column('net_weight', String(225)),	
# Column('unit_of_weight', String(225)),	
# Column('stacking_factor', String(225)),	
# Column('material_group', String(225)),	
# Column('run_out_date', String(225)),	
# Column('proc_type', String(225)),	
# Column('part_type', String(225)),	
# Column('character', String(225)),	
# Column('init_upg', String(225)),	
# Column('init_use_type', String(225)),	
# Column('procurement_type', String(225)),	
# Column('storage_location', String(225)),	
# Column('bwd_consumption_per', String(225)),	
# Column('fwd_consumption_per', String(225)),	
# Column('pps_planning_calendar', String(225)),	
# Column('factory_calendar', String(225)),	
# Column('mrp_group', String(225)),	
# Column('mixed_mrp', String(225)),	
# Column('strategy_group', String(225)),	
# Column('consumption_mode', String(225)),	
# Column('abc_indicator', String(225)),	
# Column('spab_indicator', String(225)),	
# Column('status', String(225)),	
# Column('status_valid_from', String(225)),	
# Column('bulk_material', String(225)),	
# Column('omb_part', String(225)),	
# Column('warehouse_number', String(225)),	
# Column('storage_type_stock_placement', String(225)),	
# Column('storage_type_stock_removement', String(225)),	
# Column('release', String(225)),	
# Column('release_date', String(225)),	
# Column('release_type', String(225)),	
# Column('release_action_code', String(225)),	
# Column('active_material', String(225)),	
# Column('plant_calendar', String(225)),	
# Column('document_number', String(225)),	
# Column('sid_client', String(225)),	
# Column('snapdate', String(225)),	
# Column('snaptimestamp', String(225)),	
# Column('load_date', String(225)),	
# Column('load_timestamp', String(225)),	
# Column('_load_date', String(225))
# )


# dbExceptionManager = Table (
#                     "Exception", 
#                     meta,
#                     Column('mandt', String(225)),
#                     Column('matnr', String(225)),
#                     Column('aline', String(225)),
#                     Column('cdate', String(225)),
#                     Column('ctime', String(225)),
#                     Column('dat00', String(225)),
#                     Column('delb0', String(225)),
#                     Column('extra', String(225)),
#                     Column('umdat', String(225)),
#                     Column('auskt', Integer),
#                     Column('mng01', String(225)),
#                     Column('mng02', String(225)),
#                     Column('p_ingestday', String(225)),
#                     Column('p_ingesttime', String(225))
# 				)

# dbmd04 = Table(
#             "MD04",
#             meta,
#             Column("material", String(225)),
#             Column("plant", String(225)),
#             Column("mrp_area", String(225)),
#             Column("demand_date", String(225)),
#             Column("mrp_element_cd", String(225)),
#             Column("shipping_notification", String(225)),
#             Column("container_info", String(225)),
#             Column("mrp_element", String(225)),
#             Column("change_quantity", Integer),
#             Column("total_quantity", Integer),
#             Column("storage_location", String(225)),
#             Column("supplier_nr", String(225)),
#             Column("planner", String(225)),
#             Column("split_indicator", String(225)),
#             Column("line_index", String(225)),
#             Column("document_uuid", String(225)),
#             Column("sid_client", String(225)),
#             Column("snapdate", String(225)),
#             Column("snaptime", String(225)),
#             Column("load_date", String(225)),
#             Column("load_timestamp", String(225)),
#             Column("_load_date", String(225))
#     )

# dbZgrve = Table(
#         "Zgrve",
#         meta,
#         Column("mandt", String(225)),
#         Column("lifnr", String(225)),
#         Column("delnote", String(225)),
#         Column("trailer", String(225)),
#         Column("matnr", String(225)),
#         Column("mblnr", String(225)),
#         Column("itmno", String(225)),
#         Column("erdat", String(225)),
#         Column("erfmg", String(225)),
#         Column("meins", String(225)),
#         Column("ebeln", String(225)),
#         Column("ebelp", String(225)),
#         Column("werks", String(225)),
#         Column("lgort", String(225)),
#         Column("bwart", String(225)),
#         Column("rct_ident", String(225)),
#         Column("crttime", String(225)),
#         Column("status", String(225)),
#         Column("shkzg", String(225)),
#         Column("vbeln", String(225)),
#         Column("bolnr", String(225)),
#         Column("p_ingestday", String(225)),
#         Column("p_ingesttime", String(225))
# )





                  
# meta.create_all(engine) 