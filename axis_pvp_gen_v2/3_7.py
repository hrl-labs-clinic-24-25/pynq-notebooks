class AxiPvpGen(SocIp):
    
    # PVP Gen Control Registers
    
    # X_AXIS_START_VAL_0_REG : 20 bit
    # Y_AXIS_START_VAL_1_REG : 20 bit
    # Z_AXIS_START_VAL_2_REG : 20 bit
    # W_AXIS_START_VAL_3_REG : 20 bit
    
    # TRIGGER_PVP_REG: 1 bit
    
    # DWELL_CYCLES_REG : 16 bit
    # CYCLES_TILL_READOUT : 16 bit
    
    # STEP_SIZE_REG : 20 bit
    # PVP_WIDTH_REG : 10 bit
    # NUM_DACS_REG : 3 bits
    
    # W_REG_W : 6 bit (dac that changes value every cycle) (demuxing)
    # W_REG_X : 6 bit (dac that changes value every depth^1 cycles)
    # W_REG_Y : 6 bit (dac that changes value every depth^2 cycles)
    # W_REG_Z : 6 bit (dac that changes value every depth^3 cycles)
    
    ## READ_ONLY REGISTER
    # mosi_o : 32 bit
    
    
    bindto = ['user.org:user:axi_pvp_gen_v2:1.0']
    
    def __init__(self, description, **kwargs):
        super().__init__(description)
        
        #map register names to offsets
        self.REGISTERS = {
            'start_val_0_reg':0, #THESE WILL PROBABLY BE RENAMED TO X_AXIS_START_VAL, etc
            'start_val_1_reg':1,
            'start_val_2_reg':2,
            'start_val_3_reg':3,
            'trigger_pvp_reg':4,
            'dwell_cycles_reg':5,
            'cycles_till_readout_reg':6,
            'step_size_reg':7,
            'pvp_width_reg':8,
            'num_dacs_reg':9,
            'w_reg_w':10, # PROBABLY RENAMING THESE TO X_AXIS_DEMUX_REG too, pending liaison approval
            'w_reg_x':11,
            'w_reg_y':12,
            'w_reg_z':13,
            'mosi':14
        }
        
        #default register values
        self.start_val_0_reg = 0
        self.start_val_1_reg = 0
        self.start_val_2_reg = 0
        self.start_val_3_reg = 0
        self.trigger_pvp_reg = 0
        self.dwell_cycles_reg = 38400 # at board speed of 384 MHz, 38400 dwell cycles is 100 us
        self.step_size_reg = 0
        self.pvp_width_reg = 256
        self.num_dacs_reg = 0 # set to 0 for manual control?
        self.w_reg_w = -1 # if we haven't chosen which demux dac number to be dac_w, then we don't want to accidentally change a random dac by leaving this memory unset
        self.w_reg_x = -1
        self.w_reg_y = -1
        self.w_reg_z = -1
        # mosi is read only so we don't give it a default here
        
        
    
    def set_start(self, axis = '', start_val = 0):
        '''method to set start val 
            (note that we want a method for this because we don't want to worry about registers outside this class)'''
        if (axis == 'X'):
            self.x_axis_start_reg = start_val
        elif (axis == 'Y'):
            self.y_axis_start_reg = start_val
        elif (axis == 'Z'):
            self.y_axis_start_reg = start_val
        elif (axis == 'W'):
            self.y_axis_start_reg = start_val
        else:
            raise ValueError("No valid axis was specified. Valid axis arguments are 'X', 'Y', 'Z', 'W'")
       
        
    def set_step_size(self, step_size = 0):
        '''sets size of step (in Volts??)'''
        self.step_size_reg = step_size
        
    def set_pvp_width(self, pvp_width = 256): #this default value is so if someone accidentally runs the method without a argument, the new value is just the default reset value
        '''sets the width in pixels of a pvp'''
        self.pvp_width_reg = pvp_width
        
    def set_num_dacs(self, num_dacs = 0):
        self.num_dacs_reg = num_dacs