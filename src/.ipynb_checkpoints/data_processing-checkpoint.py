import pandas as pd

def prepare_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Rename columns and apply sign correction to force data.
    """
    df = df.copy()

    df.columns = ['time', 'Fx', 'timey', 'Fy', 'timex', 'Fz']
    df['Fx'] = -df['Fx']
    df['Fz'] = -df['Fz']

    return df


def get_mean(df: pd.DataFrame) -> dict:
    """
    Compute mean values of force components.
    """
    return {
        'Fx': df['Fx'].mean(),
        'Fy': df['Fy'].mean(),
        'Fz': df['Fz'].mean()
    }
    
def apply_scaling(df: pd.DataFrame, factor: float) -> pd.DataFrame:
    """
    Apply multiplication factor to force components.
    """
    df = df.copy()
    df['Fx'] = df['Fx'] * factor
    df['Fy'] = df['Fy'] * factor
    df['Fz'] = df['Fz'] * factor
    return df