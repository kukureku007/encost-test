create view result_view as
with full_periods as (
	select
		endpoint_id,
		mode_start,
		mode_start + (mode_duration * interval '1 minute') as mode_end,
		mode_duration,
		label
	from periods
)
select
	full_periods.endpoint_id,
	full_periods.mode_start,
	full_periods.mode_end,
	full_periods.mode_duration,
	full_periods.label,
	coalesce(reason, 'Нет данных') as reason,
	operator_name,
	sum(energy.kwh) as energy_sum
from full_periods
left join energy
	on energy.event_time between full_periods.mode_start and full_periods.mode_end
	and full_periods.endpoint_id = energy.endpoint_id
left join reasons
	on reasons.event_time between full_periods.mode_start and full_periods.mode_end
	and full_periods.endpoint_id = reasons.endpoint_id
left join operators
	on login_time <= full_periods.mode_start
	and logout_time >= full_periods.mode_end
	and full_periods.endpoint_id = operators.endpoint_id
group by 1,2,3,4,5,6,7;

SET TIME ZONE 'Europe/Moscow';
select * from result_view;