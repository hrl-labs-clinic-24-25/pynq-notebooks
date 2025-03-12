class AxiPvpGen(SocIp):
    
    # PVP Gen Control Registers
    
    # START_VAL_0_REG : 20 bit
    # START_VAL_1_REG : 20 bit
    # START_VAL_2_REG : 20 bit
    # START_VAL_3_REG : 20 bit
    
    # TRIGGER_PVP_REG: 1 bit
    
    # DWELL_CYCLES_REG : 16 bit
    # CYCLES_TILL_READOUT : 16 bit
    # STEP_SIZE_REG : 20 bit
    # PVP_WIDTH_REG : 10 bit
    # NUM_DIMS_REG : 3 bits
    
    # DEMUX_0_REG : 6 bit (dac that changes value every cycle) (demuxing)
    # DEMUX_1_REG : 6 bit (dac that changes value every depth^1 cycles)
    # DEMUX_2_REG : 6 bit (dac that changes value every depth^2 cycles)
    # DEMUX_3_REG : 6 bit (dac that changes value every depth^3 cycles)
    
    ## READ_ONLY REGISTER
    # mosi_o : 32 bit
    
    
    bindto = ['user.org:user:axi_pvp_gen_v2:2.0']
    
    def __init__(self, description, **kwargs):
        super().__init__(description)
        
        #map register names to offsets
        self.REGISTERS = {
            'start_val_0_reg':0, 
            'start_val_1_reg':1,
            'start_val_2_reg':2,
            'start_val_3_reg':3,
            'trigger_pvp_reg':4,
            'dwell_cycles_reg':5,
            'cycles_till_readout_reg':6,
            'step_size_reg':7,
            'pvp_width_reg':8,
            'num_dims_reg':9,
            'demux_0_reg':10, 
            'demux_1_reg':11,
            'demux_2_reg':12,
            'demux_3_reg':13,
            'mosi':14
        }
        
        #default register values
        self.start_val_0_reg = 0
        self.start_val_1_reg = 0.456
        self.start_val_2_reg = 0
        self.start_val_3_reg = 0
        
        self.trigger_pvp_reg = 0
        self.dwell_cycles_reg = 38400 # at board speed of 384 MHz, 38400 dwell cycles is 100 us
        self.step_size_reg = 0
        self.pvp_width_reg = 256
        self.num_dims_reg = 0 # set to 0 for manual control?
        
        self.demux_0_reg = -1 # if we haven't chosen which demux dac number to be dac_w, then we don't want to accidentally change a random dac by leaving this memory unset
        self.demux_1_reg = -1
        self.demux_2_reg = -1
        self.demux_3_reg = -1
        # mosi is read only so we don't give it a default here
        
        
    
    def set_start(self, axis = '', start_val = 0.123):
        '''method to set start val 
            (note that we want a method for this because we don't want to worry about registers outside this class)'''
        if (axis == '0'):
            self.start_val_0_reg = start_val
        elif (axis == '1'):
            self.start_val_1_reg = start_val
        elif (axis == '2'):
            self.start_val_2_reg = start_val
        elif (axis == '3'):
            self.start_val_3_reg = start_val
        else:
            raise ValueError("No valid axis was specified. Valid axis arguments are '0', '1', '2', '3'")
       
    ## TODO: trigger source method. or maybe that gets set in some initialization routine?
    ## TODO: methods for start_pvp, set_dwell_cycles
    
    def set_step_size(self, step_size = 0):
        '''sets size of step (in Volts??)'''
        self.step_size_reg = step_size
        
    def set_pvp_width(self, pvp_width = 256): #this default value is so if someone accidentally runs the method without a argument, the new value is just the default reset value
        '''sets the width in pixels of a pvp'''
        self.pvp_width_reg = pvp_width
        
    def set_num_dims(self, num_dims = 0):
        self.num_dim_reg = num_dims
        
    def set_demux(self, axis = '', demux = -1): 
        #note to self: do we specify demux value or ask for board num and dac num?
        if (demux > 0 and demux < 32):
            if (axis == '0'):
                self.start_val_0_reg = demux
            elif (axis == '1'):
                self.start_val_1_reg = demux
            elif (axis == '2'):
                self.start_val_2_reg = demux
            elif (axis == '3'):
                self.start_val_3_reg = demux
            else:
                raise ValueError("No valid axis was specified. Valid axis arguments are '0', '1', '2', '3'")
        else:
            raise ValueError("Demux value must be in the range 0-31 inclusive")
            
    