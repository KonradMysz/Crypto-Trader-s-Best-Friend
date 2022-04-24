import BinanceData as bd
import Calcs as cs
import Plots as pts
import Behaviour as bh

driver = 'THANKS'

while (driver != 'THANKS'):
    driver = input("It was inappropriate. Please enter THANKS to go to the main menu.")

while (driver == 'THANKS'):
    print()
    print('Welcome Crypto Trader. Please enter symbol You want to check (e.g. BTCUSDT) or enter SYMBOLS to see list of available symbols.,', "\n")
    command_1 = input("Symbol: ")
    
    if (command_1 == 'SYMBOLS'):
        print('Available symbols are: ')
        print(bd.get_symbols())
        command_1 = '';

    elif command_1 in bd.get_symbols():
        command_2 = input("Please select interval (1m/3m/5m/15m/30m/1h/2h/4h/1d/1w): ")
        intervals = ['1m', '3m', '5m', '15m', '30m', '1h', '2h', '4h', '1d', '1w']

        if command_2 in intervals:
            data = bd.get_bars(command_1, command_2)
            print('You selected ' + command_1 + ' on interval ' + command_2 + '. Here are Your options:', "\n")
            print('Enter BASIC to see basic candlestick plot with volume barplot for the symbol.')
            print('Enter SMA to calculate and plot Simple Moving Averages (20, 50 and 100 periods) for the symbol.')
            print('Enter EMA to calculate and plot Exponential Moving Averages (20, 50 and 100 periods) for the symbol.')
            print('Enter RSI to calculate and plot Relative Strength Index indicator for the symbol.')
            print('Enter BOLL to calculate and plot Bollinger Bands for the symbol.')
            print('Enter MACD to calculate and plot Moving Average Convergence / Divergence for the symbol.')
            print('Enter MOM to calculate and plot Momentum indicator for the symbol.')
            print('Enter STOCH to calculate and plot Stochastic RSI indicator for the symbol.')
            print('Enter SUMMARY to display brief summary and some simple remarks about the symbol')
            command_3 = input('So, what do You select? ')

            if command_3 == 'BASIC':
                bh.run_basic(data)
            elif command_3 == 'SMA':
                bh.run_sma(data)
            elif command_3 == 'EMA':
                bh.run_ema(data)
            elif command_3 == 'RSI':
                bh.run_rsi(data)
            elif command_3 == 'BOLL':
                bh.run_boll(data)
            elif command_3 == 'MACD':
                bh.run_macd(data)
            elif command_3 == 'MOM':
                bh.run_mom(data)
            elif command_3 == 'STOCH':
                bh.run_stoch(data)
            elif command_3 == 'SUMMARY':
                bh.run_summary(data, command_1)
            else:
                print('This is not a valid command. Valid commands are: BASIC/SMA/EMA/RSI/BOLL/MACD/MOM/STOCH/SUMMARY')
                command_3 = input('So, what do You select? ')
        else:
            print("This is not a valid interval. Please select one of the following: 1m/3m/5m/15m/30m/1h/2h/4h/1d/1w ")
    else:
        print("This is not a valid symbol. Please enter symbol You want to check (e.g. BTCUSDT) or enter SYMBOLS to see list of available symbols: ")

