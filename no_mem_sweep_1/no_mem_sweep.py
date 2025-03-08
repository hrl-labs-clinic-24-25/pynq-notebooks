class AxisNoMemSweep(SocIp):
    
    # No Mem Sweep Control Registers
    # START_VAL_REG : 20 bit
    # STEP_SIZE_REG : 20 bit
    
    bindto = ['user.org:user:axis_no_mem_sweep:1.0']
    
    def __init__(self, description, **kwargs):
        super().__init__(description)
        
        #map register names to offsets
        self.REGISTERS = {
            'start_val_reg':0,
            'step_size_reg':1}
        
        #default register values
        self.start_val_reg = 0
        self.step_size_reg = 0
    
    def set_start(self, start_val = 0):
        '''method to set start val 
            (note that we want a method for this because we don't want to worry about registers outside this class)'''
        self.start_val_reg = start_val
        
    def set_step_size(self, step_size = 0):
        '''sets size of step (in Volts??)'''
        self.step_size_reg = step_size




class TestSoc(Overlay):
    def __init__(self, bitfile=None, **kwargs):
        if bitfile is None:
            Overlay.__init__(self, bitfile_path(), **kwargs)
        else:
            Overlay.__init__(self, bitfile, **kwargs)
        

        
# to access through the magical bindto and overlay
no_mem_sweep_1 = TestSoc()
no_mem_sweep_1.axis_no_mem_sweep_0