library verilog;
use verilog.vl_types.all;
entity ControlLED is
    port(
        d1              : in     vl_logic;
        y               : out    vl_logic
    );
end ControlLED;
