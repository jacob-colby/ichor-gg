---
type: smite-build
god: Fenrir
mode: Conquest
builds:
- source: community
  aspect: Aspect of Loyalty
  aspect_pick_rate: 0.06
  aspect_win_rate: 0.67
  slot_order:
  - name: Jotunn's Revenge
    pick_rate: 0.52
    win_rate: 0.42
    alternates:
    - name: Golden Blade
      pick_rate: 0.11
      win_rate: 0.7
    - name: The Reaper
      pick_rate: 0.09
      win_rate: 0.88
  - name: Shifter's Shield
    pick_rate: 0.4
    win_rate: 0.54
    alternates:
    - name: Barbed Carver
      pick_rate: 0.08
      win_rate: 0.29
    - name: Jotunn's Revenge
      pick_rate: 0.06
      win_rate: 0.5
  - name: Kinetic Cuirass
    pick_rate: 0.2
    win_rate: 0.5
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.09
      win_rate: 0.88
    - name: Hydra's Lament
      pick_rate: 0.08
      win_rate: 0.43
  - name: Hide of the Nemean Lion
    pick_rate: 0.16
    win_rate: 0.71
    alternates:
    - name: Heartseeker
      pick_rate: 0.08
      win_rate: 0.43
    - name: Sundering Echo
      pick_rate: 0.07
      win_rate: 0.5
  - name: Shell of Rebuke
    pick_rate: 0.09
    win_rate: 1.0
    alternates:
    - name: Titan's Bane
      pick_rate: 0.08
      win_rate: 0.33
    - name: Hide of the Nemean Lion
      pick_rate: 0.08
      win_rate: 0.83
  - name: Engraved Guard
    pick_rate: 0.1
    win_rate: 0.6
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.0
    - name: The Reaper
      pick_rate: 0.04
      win_rate: 1.0
  community_starters:
  - name: Hunter's Cowl
    pick_rate: 0.33
    win_rate: 0.61
  - name: Leather Cowl
    pick_rate: 0.14
    win_rate: 0.23
  - name: Bumba's Hammer
    pick_rate: 0.12
    win_rate: 0.55
  source_url: https://smitebrain.com/gods/fenrir/
  last_verified: '2026-09-12'
  god_win_rate: 0.5483870967741935
  god_matches_won: 51
  god_matches_played: 93
  god_division: obsidian
  god_window_start: '2026-09-08'
  god_window_end: '2026-09-12'
  god_matches_analyzed: 4284
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Golden Blade
  - Jotunn's Revenge
  - The Reaper
  - Pendulum Blade
  - The Crusher
  - Avatar's Parashu
  flex_slots:
  - Pendulum Blade
  - Avatar's Parashu
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Shell of Rebuke — magical protection
    swap_item: Shell of Rebuke
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: The Reaper, Golden Blade, The Crusher, Pendulum Blade, Avatar''s Parashu,
    Heartseeker, Tekko-Kagi, Tyrfing, Hydra''s Lament, Arondight, Transcendence, Runeforged
    Hammer, Avenging Blade, Lernaean Bow, Shield Splitter, Dominance, Silverbranch
    Bow, Oath-Sworn Spear, Riptalon, Toxic Blade, Bloodforge, Deathbringer, Eye of
    the Storm, Damaru, Rage, Musashi''s Dual Swords, Sanguine Lash, Barbed Carver.'
  slot_scores:
    Golden Blade:
      total: 0.56
      efficiency: 0.39
      win: 0.7
      pick: 0.11
      fit: 0.67
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.42
      pick: 0.52
      fit: 1.0
    The Reaper:
      total: 0.77
      efficiency: 0.5
      win: 1.0
      pick: 0.12
      fit: 0.91
    Pendulum Blade:
      total: 0.52
      efficiency: 0.42
      win: 0.5
      pick: 0.0
      fit: 1.0
    The Crusher:
      total: 0.54
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 1.0
    Avatar's Parashu:
      total: 0.52
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.91
  community_ordered:
  - Golden Blade
  - Jotunn's Revenge
  - The Reaper
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Golden Blade
  - Jotunn's Revenge
  - Hydra's Lament
  - Shell of Rebuke
  - The Reaper
  - Heartseeker
  flex_slots:
  - Hydra's Lament
  - Heartseeker
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Hide of the Nemean Lion — physical protection
    swap_item: Hide of the Nemean Lion
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: The
    Reaper, Golden Blade, Hydra''s Lament, Heartseeker, The Crusher, Transcendence,
    Arondight, Pendulum Blade, Avatar''s Parashu, Runeforged Hammer, Tyrfing, Tekko-Kagi,
    Avenging Blade, Dominance, Breastplate of Valor, Lernaean Bow, Genji''s Guard,
    Shield Splitter, Oath-Sworn Spear, Daybreak Gavel, Silverbranch Bow, Bloodforge,
    Riptalon, Yogi''s Necklace, Toxic Blade, Deathbringer, Eye of the Storm, Barbed
    Carver.'
  slot_scores:
    Golden Blade:
      total: 0.51
      efficiency: 0.39
      win: 0.7
      pick: 0.11
      fit: 0.35
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.42
      pick: 0.52
      fit: 0.71
    Hydra's Lament:
      total: 0.48
      efficiency: 0.54
      win: 0.43
      pick: 0.12
      fit: 0.63
    Shell of Rebuke:
      total: 0.5
      efficiency: 0.13
      win: 1.0
      pick: 0.19
      fit: 0.0
    The Reaper:
      total: 0.7
      efficiency: 0.5
      win: 1.0
      pick: 0.12
      fit: 0.47
    Heartseeker:
      total: 0.48
      efficiency: 0.47
      win: 0.43
      pick: 0.13
      fit: 0.77
  community_ordered:
  - Golden Blade
  - Jotunn's Revenge
  - Hydra's Lament
  - Shell of Rebuke
  - The Reaper
  - Heartseeker
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Golden Blade
  - Jotunn's Revenge
  - Shell of Rebuke
  - The Reaper
  - Pendulum Blade
  - The Crusher
  flex_slots:
  - Pendulum Blade
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Hide of the Nemean Lion — physical protection
    swap_item: Hide of the Nemean Lion
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: The Reaper, Golden Blade, Pendulum Blade, The Crusher, Heartseeker, Hydra''s
    Lament, Arondight, Avatar''s Parashu, Tekko-Kagi, Transcendence, Runeforged Hammer,
    Tyrfing, Avenging Blade, Silverbranch Bow, Breastplate of Valor, Riptalon, Genji''s
    Guard, Lernaean Bow, Toxic Blade, Shield Splitter, Dominance, Daybreak Gavel,
    Oath-Sworn Spear, Eye of Erebus, Screeching Gargoyle, Bloodforge, Chandra''s Grace,
    Barbed Carver.'
  slot_scores:
    Golden Blade:
      total: 0.5
      efficiency: 0.39
      win: 0.7
      pick: 0.11
      fit: 0.29
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.42
      pick: 0.52
      fit: 0.78
    Shell of Rebuke:
      total: 0.5
      efficiency: 0.13
      win: 1.0
      pick: 0.19
      fit: 0.0
    The Reaper:
      total: 0.71
      efficiency: 0.5
      win: 1.0
      pick: 0.12
      fit: 0.56
    Pendulum Blade:
      total: 0.49
      efficiency: 0.42
      win: 0.5
      pick: 0.0
      fit: 0.78
    The Crusher:
      total: 0.49
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.66
  community_ordered:
  - Golden Blade
  - Jotunn's Revenge
  - Shell of Rebuke
  - The Reaper
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Golden Blade
  - Shifter's Shield
  - Shell of Rebuke
  - Hide of the Nemean Lion
  - The Reaper
  - Amanita Charm
  flex_slots:
  - Golden Blade
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: The Reaper, Amanita Charm, Shield of the Phoenix, Runeforged Hammer,
    Shield Splitter, Eye of the Storm, Freya''s Tears, Berserker''s Shield, Erosion,
    Eye of Providence, Genji''s Guard, Breastplate of Valor, Draconic Scale, Yogi''s
    Necklace, Phoenix Feather, Avenging Blade, Stone of Binding, Midgardian Mail,
    Chandra''s Grace, Daybreak Gavel, The Crusher, Magi''s Cloak, Leviathan''s Hide,
    Heartseeker, Hydra''s Lament.'
  slot_scores:
    Golden Blade:
      total: 0.55
      efficiency: 0.44
      win: 0.7
      pick: 0.11
      fit: 0.51
    Shifter's Shield:
      total: 0.55
      efficiency: 0.55
      win: 0.54
      pick: 0.55
      fit: 0.56
    Shell of Rebuke:
      total: 0.61
      efficiency: 0.28
      win: 1.0
      pick: 0.19
      fit: 0.34
    Hide of the Nemean Lion:
      total: 0.57
      efficiency: 0.52
      win: 0.71
      pick: 0.27
      fit: 0.39
    The Reaper:
      total: 0.73
      efficiency: 0.5
      win: 1.0
      pick: 0.12
      fit: 0.7
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.86
  community_ordered:
  - Golden Blade
  - Shifter's Shield
  - Shell of Rebuke
  - Hide of the Nemean Lion
  - The Reaper
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Golden Blade
  - Jotunn's Revenge
  - The Reaper
  - Pendulum Blade
  - The Crusher
  - Avatar's Parashu
  flex_slots:
  - Pendulum Blade
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Shell of Rebuke — magical protection
    swap_item: Shell of Rebuke
  - vs_tag: physical_heavy
    swap: Hide of the Nemean Lion — physical protection
    swap_item: Hide of the Nemean Lion
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: The Reaper, The Crusher, Avatar''s Parashu, Pendulum Blade, Golden
    Blade, Heartseeker, Tekko-Kagi, Avenging Blade, Silverbranch Bow, Riptalon, Hydra''s
    Lament, Oath-Sworn Spear, Tyrfing, Transcendence, Arondight, Toxic Blade, Runeforged
    Hammer, Lernaean Bow, Shield Splitter, Dominance, Screeching Gargoyle, Daybreak
    Gavel, Bloodforge, Breastplate of Valor, Genji''s Guard, Deathbringer, Eye of
    the Storm, Barbed Carver.'
  slot_scores:
    Golden Blade:
      total: 0.52
      efficiency: 0.39
      win: 0.7
      pick: 0.11
      fit: 0.42
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.42
      pick: 0.52
      fit: 1.0
    The Reaper:
      total: 0.77
      efficiency: 0.5
      win: 1.0
      pick: 0.12
      fit: 0.94
    Pendulum Blade:
      total: 0.52
      efficiency: 0.42
      win: 0.5
      pick: 0.0
      fit: 1.0
    The Crusher:
      total: 0.54
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 1.0
    Avatar's Parashu:
      total: 0.52
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.94
  community_ordered:
  - Golden Blade
  - Jotunn's Revenge
  - The Reaper
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Jotunn's Revenge
  - Tyrfing
  - The Reaper
  - Riptalon
  - Silverbranch Bow
  flex_slots:
  - Tyrfing
  - Silverbranch Bow
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shell of Rebuke — magical protection
    swap_item: Shell of Rebuke
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: The Reaper, Golden Blade, Riptalon, Tyrfing, Silverbranch Bow, Tekko-Kagi,
    Lernaean Bow, Toxic Blade, Dominance, Qin''s Blade, The Crusher, Sun Beam Bow,
    Heartseeker, Hydra''s Lament, Transcendence, Berserker''s Shield, Avatar''s Parashu,
    Dagger of Frenzy, Arondight, Runeforged Hammer, Pendulum Blade, Avenging Blade,
    Vital Amplifier, Hastened Fatalis, Bloodforge, The Executioner, Odysseus'' Bow,
    Barbed Carver.'
  slot_scores:
    Golden Blade:
      total: 0.59
      efficiency: 0.47
      win: 0.7
      pick: 0.11
      fit: 0.69
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.72
      win: 0.42
      pick: 0.52
      fit: 0.37
    Tyrfing:
      total: 0.51
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.79
    The Reaper:
      total: 0.71
      efficiency: 0.55
      win: 1.0
      pick: 0.12
      fit: 0.44
    Riptalon:
      total: 0.52
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.79
    Silverbranch Bow:
      total: 0.51
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.69
  community_ordered:
  - Golden Blade
  - Jotunn's Revenge
  - The Reaper
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Shell of Rebuke
  - The Reaper
  - Arondight
  - Pendulum Blade
  flex_slots:
  - Pendulum Blade
  - Arondight
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: The Reaper, Hydra''s Lament, Pendulum
    Blade, Arondight, Golden Blade, Breastplate of Valor, Genji''s Guard, The Crusher,
    Heartseeker, Avatar''s Parashu, Eye of Erebus, Transcendence, Tyrfing, Screeching
    Gargoyle, Runeforged Hammer, Chandra''s Grace, Freya''s Tears, Tekko-Kagi, Avenging
    Blade, Shield of the Phoenix, Silverbranch Bow, Daybreak Gavel, Lernaean Bow,
    Riptalon, Gladiator''s Shield, Shield Splitter, Dominance, Prophetic Cloak.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.42
      pick: 0.52
      fit: 0.85
    Hydra's Lament:
      total: 0.5
      efficiency: 0.54
      win: 0.43
      pick: 0.12
      fit: 0.75
    Shell of Rebuke:
      total: 0.5
      efficiency: 0.13
      win: 1.0
      pick: 0.19
      fit: 0.0
    The Reaper:
      total: 0.68
      efficiency: 0.5
      win: 1.0
      pick: 0.12
      fit: 0.35
    Arondight:
      total: 0.5
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.65
    Pendulum Blade:
      total: 0.5
      efficiency: 0.42
      win: 0.5
      pick: 0.0
      fit: 0.85
  community_ordered:
  - Jotunn's Revenge
  - Hydra's Lament
  - Shell of Rebuke
  - The Reaper
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - The Reaper
  - Pendulum Blade
  - The Crusher
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - The Reaper
  - Pendulum Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: The Crusher, Heartseeker, The Reaper, Pendulum Blade,
    Hydra''s Lament, Avatar''s Parashu, Tekko-Kagi, Tyrfing, Arondight, Transcendence,
    Runeforged Hammer, Avenging Blade, Golden Blade, Lernaean Bow, Shield Splitter,
    Dominance, Silverbranch Bow, Oath-Sworn Spear, Riptalon, Barbed Carver, Toxic
    Blade, Bloodforge, Deathbringer, Eye of the Storm, Damaru, Rage, Musashi''s Dual
    Swords, Sanguine Lash.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.42
      pick: 0.52
      fit: 1.0
    The Reaper:
      total: 0.77
      efficiency: 0.5
      win: 1.0
      pick: 0.12
      fit: 0.91
    Pendulum Blade:
      total: 0.52
      efficiency: 0.42
      win: 0.5
      pick: 0.0
      fit: 1.0
    The Crusher:
      total: 0.54
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 1.0
    Heartseeker:
      total: 0.51
      efficiency: 0.47
      win: 0.43
      pick: 0.13
      fit: 1.0
    Titan's Bane:
      total: 0.47
      efficiency: 0.47
      win: 0.33
      pick: 0.17
      fit: 1.0
  community_ordered:
  - Jotunn's Revenge
  - The Reaper
  - Heartseeker
  - Titan's Bane
  starter: *id001
---
