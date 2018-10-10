library verilog;
use verilog.vl_types.all;
entity Extend is
    port(
        InstrD          : in     vl_logic_vector(23 downto 0);
        ImmSrcD         : in     vl_logic_vector(1 downto 0);
        ExtImm          : out    vl_logic_vector(31 downto 0)
    );
end Extend;
