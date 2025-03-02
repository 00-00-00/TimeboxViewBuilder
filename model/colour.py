class HexToRGBTransformer:
    def transform(value):
        return (
            (value >> 16) & 0xFF, 
            (value >> 8) & 0xFF,
            (value >> 0) & 0xFF
        )