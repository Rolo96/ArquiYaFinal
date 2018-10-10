library verilog;
use verilog.vl_types.all;
entity Decoder is
    generic(
        BITS            : integer := 32
    );
    port(
        InstrD          : in     vl_logic_vector;
        Op              : out    vl_logic_vector(1 downto 0);
        Funct           : out    vl_logic_vector(5 downto 0);
        Rd              : out    vl_logic_vector(3 downto 0);
        CondD           : out    vl_logic_vector(3 downto 0);
        RA1D            : out    vl_logic_vector(3 downto 0);
        RA2D            : out    vl_logic_vector(3 downto 0);
        WA3D            : out    vl_logic_vector(3 downto 0);
        ExtImmD         : out    vl_logic_vector(24 downto 0)
    );
    attribute mti_svvh_generic_type : integer;
    attribute mti_svvh_generic_type of BITS : constant is 1;
end Decoder;
