import pandas as pd

def prepare_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Rename columns and apply sign correction to force data.
    """
    df = df.copy()

    df = df.loc[:, ~df.columns.astype(str).str.contains('^Unnamed')]

    
    default_headers_sim = ['time', 'Fx', 'timey', 'Fy', 'timez', 'Fz']
    default_headers_paper = ['time', 'Force']

    if df.shape[1] == 2:

        # Promote first row to header
#         df.columns = df.iloc[0]
#         df = df.iloc[1:].reset_index(drop=True)

        # Standardize column names
        df.columns = ['time', 'Force']

    # Case 2: Existing format (Fx, Fy, Fz)
    else:
        df.columns = default_headers_sim

        # Sign correction
        df['Fx'] = -df['Fx']
        df['Fz'] = -df['Fz']
        df.drop(columns=['timey','timez'], inplace=True)

    # Convert to numeric safely
    for col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    return df

def get_mean(df: pd.DataFrame) -> dict:
    """
    Compute mean values of force components.
    """
    mean_dict = {}

    for col in df.columns:
        if col.lower() != 'time':
            mean_dict[col] = df[col].mean()

    return mean_dict
    
def apply_scaling(df: pd.DataFrame, factor: float) -> pd.DataFrame:
    """
    Apply multiplication factor to force components.
    """
    df = df.copy()
    for col in df.columns:
        if col.lower() != 'time':
            df[col] = df[col] * factor
    
    return df
