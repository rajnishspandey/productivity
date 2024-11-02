from flask import Blueprint, render_template, request, jsonify
import datetime
import pytz

world_clock_bp = Blueprint('world_clock', __name__)

# Comprehensive list of timezones
TIMEZONES = [
    'US/Eastern', 'US/Pacific', 'US/Central', 'US/Mountain',
    'Europe/London', 'Europe/Paris', 'Europe/Berlin', 'Europe/Moscow',
    'Asia/Tokyo', 'Asia/Shanghai', 'Asia/Dubai', 'Asia/Singapore', 
    'Asia/Kolkata', 'Asia/Seoul', 'Asia/Taipei',
    'Australia/Sydney', 'Australia/Perth', 'Pacific/Auckland',
    'Pacific/Honolulu', 'America/Sao_Paulo', 'Africa/Cairo', 
    'Europe/Istanbul', 'Asia/Jerusalem'
]

@world_clock_bp.route('/', methods=['GET', 'POST'])
def world_clock():
    # Get current times for all timezones
    world_times = []
    for zone in TIMEZONES:
        zone_tz = pytz.timezone(zone)
        zone_time = datetime.datetime.now(zone_tz)
        world_times.append({
            'zone': zone,
            'display_name': zone.replace('/', ' - '),
            'time': zone_time.strftime('%Y-%m-%d %H:%M:%S'),
            'offset': zone_time.strftime('%z')
        })
    
    return render_template('world_clock.html', world_times=world_times)

@world_clock_bp.route('/compare', methods=['POST'])
def compare_timezones():
    base_zone = request.form.get('base_zone')
    compare_zone = request.form.get('compare_zone')
    
    if not base_zone or not compare_zone:
        return jsonify({
            'error': 'Please select both base and comparison timezones'
        }), 400
    
    try:
        # Get current time in base timezone
        base_tz = pytz.timezone(base_zone)
        base_time = datetime.datetime.now(base_tz)
        
        # Convert base time to comparison timezone
        compare_tz = pytz.timezone(compare_zone)
        compare_time = base_time.astimezone(compare_tz)
        
        # Calculate time difference
        time_diff_hours = (compare_time.utcoffset() - base_time.utcoffset()).total_seconds() / 3600
        
        return jsonify({
            'base_zone': base_zone,
            'base_time': base_time.strftime('%Y-%m-%d %H:%M:%S %Z'),
            'compare_zone': compare_zone,
            'compare_time': compare_time.strftime('%Y-%m-%d %H:%M:%S %Z'),
            'time_difference': f"{abs(time_diff_hours):.1f} hours " + 
                               ("ahead" if time_diff_hours > 0 else "behind")
        })
    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 500