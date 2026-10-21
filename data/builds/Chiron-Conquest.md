---
type: smite-build
god: Chiron
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Heroic Tutor
  aspect_pick_rate: 0.11
  aspect_win_rate: 0.2
  slot_order:
  - name: Transcendence
    pick_rate: 0.78
    win_rate: 0.6
    alternates:
    - name: Chandra's Grace
      pick_rate: 0.04
      win_rate: 0.0
    - name: Tyrfing
      pick_rate: 0.04
      win_rate: 0.5
  - name: Jotunn's Revenge
    pick_rate: 0.71
    win_rate: 0.63
    alternates:
    - name: Transcendence
      pick_rate: 0.07
      win_rate: 0.33
    - name: The Crusher
      pick_rate: 0.04
      win_rate: 0.5
  - name: Heartseeker
    pick_rate: 0.29
    win_rate: 0.54
    alternates:
    - name: The Crusher
      pick_rate: 0.2
      win_rate: 0.44
    - name: Avatar's Parashu
      pick_rate: 0.11
      win_rate: 1.0
  - name: The Crusher
    pick_rate: 0.19
    win_rate: 0.75
    alternates:
    - name: Heartseeker
      pick_rate: 0.31
      win_rate: 0.69
    - name: Titan's Bane
      pick_rate: 0.14
      win_rate: 0.67
  - name: Titan's Bane
    pick_rate: 0.16
    win_rate: 0.67
    alternates:
    - name: Heartseeker
      pick_rate: 0.16
      win_rate: 0.67
    - name: The Crusher
      pick_rate: 0.16
      win_rate: 1.0
  - name: Skeggox
    pick_rate: 0.16
    win_rate: 0.5
    alternates:
    - name: Avatar's Parashu
      pick_rate: 0.16
      win_rate: 0.5
    - name: Blinking Abyss
      pick_rate: 0.12
      win_rate: 0.67
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.4
    win_rate: 0.72
  - name: Pendulum of the Ages
    pick_rate: 0.22
    win_rate: 0.6
  - name: Bluestone Pendant
    pick_rate: 0.09
    win_rate: 0.25
  source_url: https://smitebrain.com/gods/chiron/
  last_verified: '2026-10-21'
  god_win_rate: 0.5333333333333333
  god_matches_won: 24
  god_matches_played: 45
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-10-21'
  god_matches_analyzed: 814
  starter:
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: core
  slot_order:
  - Transcendence
  - Jotunn's Revenge
  - Riptalon
  - The Crusher
  - Tekko-Kagi
  - Titan's Bane
  flex_slots:
  - Transcendence
  - Tekko-Kagi
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Riptalon, Tekko-Kagi, Lernaean Bow, The Reaper, Silverbranch Bow, Hydra''s
    Lament, Deathbringer, Golden Blade, Dominance, Demon Blade, Tyrfing, Toxic Blade,
    Musashi''s Dual Swords, Arondight, Pendulum Blade, Damaru, Rage, Runeforged Hammer,
    Qin''s Blade, Berserker''s Shield, Avenging Blade, Barbed Carver, Sun Beam Bow,
    Bloodforge.'
  slot_scores:
    Transcendence:
      total: 0.52
      efficiency: 0.53
      win: 0.6
      pick: 0.78
      fit: 0.17
    Jotunn's Revenge:
      total: 0.65
      efficiency: 0.72
      win: 0.63
      pick: 0.97
      fit: 0.44
    Riptalon:
      total: 0.52
      efficiency: 0.51
      win: 0.57
      pick: 0.0
      fit: 0.56
    The Crusher:
      total: 0.58
      efficiency: 0.47
      win: 0.75
      pick: 0.32
      fit: 0.44
    Tekko-Kagi:
      total: 0.51
      efficiency: 0.49
      win: 0.57
      pick: 0.0
      fit: 0.58
    Titan's Bane:
      total: 0.55
      efficiency: 0.47
      win: 0.67
      pick: 0.35
      fit: 0.44
  community_ordered:
  - Transcendence
  - Jotunn's Revenge
  - The Crusher
  - Titan's Bane
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: mana-stack
  slot_order:
  - Transcendence
  - Jotunn's Revenge
  - Hydra's Lament
  - Heartseeker
  - The Crusher
  - Titan's Bane
  flex_slots:
  - Heartseeker
  - Hydra's Lament
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Hydra''s
    Lament, Lernaean Bow, The Reaper, Tekko-Kagi, Riptalon, Silverbranch Bow, Dominance,
    Deathbringer, Golden Blade, Arondight, Musashi''s Dual Swords, Tyrfing, Demon
    Blade, Runeforged Hammer, Pendulum Blade, Toxic Blade, Damaru, Rage, Avenging
    Blade, Qin''s Blade, Barbed Carver, Berserker''s Shield, Breastplate of Valor,
    Genji''s Guard.'
  slot_scores:
    Transcendence:
      total: 0.53
      efficiency: 0.53
      win: 0.6
      pick: 0.78
      fit: 0.24
    Jotunn's Revenge:
      total: 0.65
      efficiency: 0.72
      win: 0.63
      pick: 0.97
      fit: 0.44
    Hydra's Lament:
      total: 0.51
      efficiency: 0.54
      win: 0.57
      pick: 0.0
      fit: 0.42
    Heartseeker:
      total: 0.51
      efficiency: 0.47
      win: 0.54
      pick: 0.45
      fit: 0.55
    The Crusher:
      total: 0.58
      efficiency: 0.47
      win: 0.75
      pick: 0.32
      fit: 0.39
    Titan's Bane:
      total: 0.54
      efficiency: 0.47
      win: 0.67
      pick: 0.35
      fit: 0.39
  community_ordered:
  - Transcendence
  - Jotunn's Revenge
  - Heartseeker
  - The Crusher
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: crit
  slot_order:
  - Jotunn's Revenge
  - Musashi's Dual Swords
  - Demon Blade
  - The Crusher
  - Deathbringer
  - Titan's Bane
  flex_slots:
  - Demon Blade
  - Musashi's Dual Swords
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Crit / auto-attack skew (efficiency + fit + win/pick). Underrated for
    this god: Riptalon, The Reaper, Silverbranch Bow, Tekko-Kagi, Lernaean Bow, Hydra''s
    Lament, Deathbringer, Demon Blade, Golden Blade, Dominance, Musashi''s Dual Swords,
    Toxic Blade, Tyrfing, Arondight, Damaru, Rage, Pendulum Blade, Qin''s Blade, Runeforged
    Hammer, Berserker''s Shield, Avenging Blade, Barbed Carver, Sun Beam Bow, Bloodforge.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.64
      efficiency: 0.72
      win: 0.63
      pick: 0.97
      fit: 0.41
    Musashi's Dual Swords:
      total: 0.48
      efficiency: 0.46
      win: 0.57
      pick: 0.0
      fit: 0.42
    Demon Blade:
      total: 0.49
      efficiency: 0.38
      win: 0.57
      pick: 0.0
      fit: 0.64
    The Crusher:
      total: 0.58
      efficiency: 0.47
      win: 0.75
      pick: 0.32
      fit: 0.42
    Deathbringer:
      total: 0.5
      efficiency: 0.51
      win: 0.57
      pick: 0.0
      fit: 0.42
    Titan's Bane:
      total: 0.55
      efficiency: 0.47
      win: 0.67
      pick: 0.35
      fit: 0.42
  community_ordered:
  - Jotunn's Revenge
  - The Crusher
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Transcendence
  - Jotunn's Revenge
  - The Reaper
  - Heartseeker
  - The Crusher
  - Titan's Bane
  flex_slots:
  - Heartseeker
  - The Reaper
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: The Reaper, Riptalon, Silverbranch Bow, Tekko-Kagi, Hydra''s Lament, Lernaean
    Bow, Deathbringer, Pendulum Blade, Dominance, Golden Blade, Arondight, Toxic Blade,
    Musashi''s Dual Swords, Tyrfing, Demon Blade, Runeforged Hammer, Damaru, Rage,
    Qin''s Blade, Avenging Blade, Berserker''s Shield, Breastplate of Valor, Barbed
    Carver, Daybreak Gavel.'
  slot_scores:
    Transcendence:
      total: 0.51
      efficiency: 0.53
      win: 0.6
      pick: 0.78
      fit: 0.13
    Jotunn's Revenge:
      total: 0.65
      efficiency: 0.72
      win: 0.63
      pick: 0.97
      fit: 0.46
    The Reaper:
      total: 0.51
      efficiency: 0.55
      win: 0.57
      pick: 0.0
      fit: 0.39
    Heartseeker:
      total: 0.51
      efficiency: 0.47
      win: 0.54
      pick: 0.45
      fit: 0.53
    The Crusher:
      total: 0.58
      efficiency: 0.47
      win: 0.75
      pick: 0.32
      fit: 0.43
    Titan's Bane:
      total: 0.55
      efficiency: 0.47
      win: 0.67
      pick: 0.35
      fit: 0.43
  community_ordered:
  - Transcendence
  - Jotunn's Revenge
  - Heartseeker
  - The Crusher
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Riptalon
  - The Crusher
  - Titan's Bane
  - Amanita Charm
  flex_slots:
  - Riptalon
  - Titan's Bane
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Berserker''s Shield, Riptalon, The Reaper, Shield of
    the Phoenix, Kinetic Cuirass, Genji''s Guard, Freya''s Tears, Breastplate of Valor,
    Runeforged Hammer, Golden Blade, Yogi''s Necklace, Shifter''s Shield, Shield Splitter,
    Lernaean Bow, Pharaoh''s Curse, Hydra''s Lament, Silverbranch Bow, Shogun''s Ofuda,
    Phoenix Feather, Eye of the Storm, Tekko-Kagi, Toxic Blade, Erosion, Daybreak
    Gavel, Eye of Providence, Tyrfing, Chandra''s Grace.'
  slot_scores:
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.57
      pick: 0.0
      fit: 0.38
    Jotunn's Revenge:
      total: 0.63
      efficiency: 0.72
      win: 0.63
      pick: 0.97
      fit: 0.3
    Riptalon:
      total: 0.54
      efficiency: 0.51
      win: 0.57
      pick: 0.0
      fit: 0.68
    The Crusher:
      total: 0.57
      efficiency: 0.47
      win: 0.75
      pick: 0.32
      fit: 0.33
    Titan's Bane:
      total: 0.53
      efficiency: 0.47
      win: 0.67
      pick: 0.35
      fit: 0.33
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.62
  community_ordered:
  - Jotunn's Revenge
  - The Crusher
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Transcendence
  - Jotunn's Revenge
  - Riptalon
  - Heartseeker
  - The Crusher
  - Titan's Bane
  flex_slots:
  - Heartseeker
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Riptalon, The Reaper, Tekko-Kagi, Silverbranch Bow, Lernaean Bow,
    Hydra''s Lament, Toxic Blade, Avenging Blade, Deathbringer, Pendulum Blade, Golden
    Blade, Dominance, Demon Blade, Tyrfing, The Executioner, Musashi''s Dual Swords,
    Arondight, Oath-Sworn Spear, Runeforged Hammer, Damaru, Rage, Qin''s Blade, Berserker''s
    Shield, Screeching Gargoyle.'
  slot_scores:
    Transcendence:
      total: 0.51
      efficiency: 0.53
      win: 0.6
      pick: 0.78
      fit: 0.14
    Jotunn's Revenge:
      total: 0.66
      efficiency: 0.72
      win: 0.63
      pick: 0.97
      fit: 0.53
    Riptalon:
      total: 0.53
      efficiency: 0.51
      win: 0.57
      pick: 0.0
      fit: 0.63
    Heartseeker:
      total: 0.53
      efficiency: 0.47
      win: 0.54
      pick: 0.45
      fit: 0.65
    The Crusher:
      total: 0.6
      efficiency: 0.47
      win: 0.75
      pick: 0.32
      fit: 0.55
    Titan's Bane:
      total: 0.57
      efficiency: 0.47
      win: 0.67
      pick: 0.35
      fit: 0.55
  community_ordered:
  - Transcendence
  - Jotunn's Revenge
  - Heartseeker
  - The Crusher
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Lernaean Bow
  - Jotunn's Revenge
  - Riptalon
  - The Crusher
  - Silverbranch Bow
  - Titan's Bane
  flex_slots:
  - Silverbranch Bow
  - Lernaean Bow
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Riptalon, Silverbranch Bow, Lernaean Bow, Tekko-Kagi, The Reaper, Golden
    Blade, Hydra''s Lament, Toxic Blade, Tyrfing, Deathbringer, Dominance, Qin''s
    Blade, Demon Blade, Musashi''s Dual Swords, Arondight, Sun Beam Bow, Pendulum
    Blade, Runeforged Hammer, Berserker''s Shield, Damaru, Rage, Avenging Blade, Dagger
    of Frenzy, Barbed Carver.'
  slot_scores:
    Lernaean Bow:
      total: 0.5
      efficiency: 0.52
      win: 0.57
      pick: 0.0
      fit: 0.45
    Jotunn's Revenge:
      total: 0.63
      efficiency: 0.72
      win: 0.63
      pick: 0.97
      fit: 0.35
    Riptalon:
      total: 0.52
      efficiency: 0.51
      win: 0.57
      pick: 0.0
      fit: 0.6
    The Crusher:
      total: 0.57
      efficiency: 0.47
      win: 0.75
      pick: 0.32
      fit: 0.36
    Silverbranch Bow:
      total: 0.52
      efficiency: 0.53
      win: 0.57
      pick: 0.0
      fit: 0.52
    Titan's Bane:
      total: 0.54
      efficiency: 0.47
      win: 0.67
      pick: 0.35
      fit: 0.36
  community_ordered:
  - Jotunn's Revenge
  - The Crusher
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Transcendence
  - Jotunn's Revenge
  - Hydra's Lament
  - The Crusher
  - Arondight
  - Titan's Bane
  flex_slots:
  - Transcendence
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
    + fit + win/pick). Underrated for this god: Hydra''s Lament, Riptalon, Silverbranch
    Bow, Lernaean Bow, The Reaper, Tekko-Kagi, Arondight, Pendulum Blade, Deathbringer,
    Dominance, Golden Blade, Toxic Blade, Breastplate of Valor, Musashi''s Dual Swords,
    Tyrfing, Genji''s Guard, Demon Blade, Qin''s Blade, Runeforged Hammer, Berserker''s
    Shield, Damaru, Rage, Avenging Blade, Daybreak Gavel.'
  slot_scores:
    Transcendence:
      total: 0.51
      efficiency: 0.53
      win: 0.6
      pick: 0.78
      fit: 0.08
    Jotunn's Revenge:
      total: 0.66
      efficiency: 0.72
      win: 0.63
      pick: 0.97
      fit: 0.49
    Hydra's Lament:
      total: 0.52
      efficiency: 0.54
      win: 0.57
      pick: 0.0
      fit: 0.46
    The Crusher:
      total: 0.56
      efficiency: 0.47
      win: 0.75
      pick: 0.32
      fit: 0.31
    Arondight:
      total: 0.49
      efficiency: 0.5
      win: 0.57
      pick: 0.0
      fit: 0.36
    Titan's Bane:
      total: 0.53
      efficiency: 0.47
      win: 0.67
      pick: 0.35
      fit: 0.31
  community_ordered:
  - Transcendence
  - Jotunn's Revenge
  - The Crusher
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Lernaean Bow
  - Jotunn's Revenge
  - The Reaper
  - Riptalon
  - Silverbranch Bow
  - Tekko-Kagi
  flex_slots:
  - The Reaper
  - Silverbranch Bow
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Riptalon, Tekko-Kagi, Lernaean Bow, The Reaper, Silverbranch
    Bow, Tyrfing, Hydra''s Lament, Deathbringer, Golden Blade, Dominance, Demon Blade,
    Toxic Blade, Musashi''s Dual Swords, Arondight, Pendulum Blade, Damaru, Rage,
    Runeforged Hammer, Qin''s Blade, Berserker''s Shield, Avenging Blade, Barbed Carver,
    Sun Beam Bow, Bloodforge.'
  slot_scores:
    Lernaean Bow:
      total: 0.51
      efficiency: 0.52
      win: 0.57
      pick: 0.0
      fit: 0.5
    Jotunn's Revenge:
      total: 0.65
      efficiency: 0.72
      win: 0.63
      pick: 0.97
      fit: 0.44
    The Reaper:
      total: 0.51
      efficiency: 0.55
      win: 0.57
      pick: 0.0
      fit: 0.43
    Riptalon:
      total: 0.52
      efficiency: 0.51
      win: 0.57
      pick: 0.0
      fit: 0.56
    Silverbranch Bow:
      total: 0.51
      efficiency: 0.53
      win: 0.57
      pick: 0.0
      fit: 0.47
    Tekko-Kagi:
      total: 0.51
      efficiency: 0.49
      win: 0.57
      pick: 0.0
      fit: 0.58
  community_ordered:
  - Jotunn's Revenge
  starter: *id001
- source: suggested
  archetype: core
  slot_order:
  - Transcendence
  - Jotunn's Revenge
  - The Reaper
  - Heartseeker
  - The Crusher
  - Titan's Bane
  flex_slots:
  - Transcendence
  - Heartseeker
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: The Reaper, Hydra''s Lament, Deathbringer, Riptalon, Tekko-Kagi, Silverbranch
    Bow, Lernaean Bow, Musashi''s Dual Swords, Pendulum Blade, Arondight, Damaru,
    Rage, Demon Blade, Golden Blade, Dominance, Runeforged Hammer, Tyrfing, Toxic
    Blade, Barbed Carver, Avenging Blade, Bloodforge, Qin''s Blade, Shield Splitter,
    Breastplate of Valor.'
  slot_scores:
    Transcendence:
      total: 0.52
      efficiency: 0.53
      win: 0.6
      pick: 0.78
      fit: 0.2
    Jotunn's Revenge:
      total: 0.66
      efficiency: 0.72
      win: 0.63
      pick: 0.97
      fit: 0.53
    The Reaper:
      total: 0.53
      efficiency: 0.55
      win: 0.57
      pick: 0.0
      fit: 0.53
    Heartseeker:
      total: 0.52
      efficiency: 0.47
      win: 0.54
      pick: 0.45
      fit: 0.61
    The Crusher:
      total: 0.59
      efficiency: 0.47
      win: 0.75
      pick: 0.32
      fit: 0.51
    Titan's Bane:
      total: 0.56
      efficiency: 0.47
      win: 0.67
      pick: 0.35
      fit: 0.51
  community_ordered:
  - Transcendence
  - Jotunn's Revenge
  - Heartseeker
  - The Crusher
  - Titan's Bane
  starter: *id001
  aspect: Aspect of the Heroic Tutor
- source: suggested
  archetype: mana-stack
  slot_order:
  - Transcendence
  - Jotunn's Revenge
  - Hydra's Lament
  - Heartseeker
  - The Crusher
  - Titan's Bane
  flex_slots:
  - Heartseeker
  - Hydra's Lament
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Hydra''s
    Lament, The Reaper, Deathbringer, Lernaean Bow, Tekko-Kagi, Riptalon, Arondight,
    Musashi''s Dual Swords, Dominance, Silverbranch Bow, Pendulum Blade, Runeforged
    Hammer, Golden Blade, Damaru, Rage, Avenging Blade, Tyrfing, Demon Blade, Barbed
    Carver, Breastplate of Valor, Toxic Blade, Bloodforge, Genji''s Guard, Shield
    Splitter.'
  slot_scores:
    Transcendence:
      total: 0.53
      efficiency: 0.53
      win: 0.6
      pick: 0.78
      fit: 0.27
    Jotunn's Revenge:
      total: 0.66
      efficiency: 0.72
      win: 0.63
      pick: 0.97
      fit: 0.5
    Hydra's Lament:
      total: 0.52
      efficiency: 0.54
      win: 0.57
      pick: 0.0
      fit: 0.47
    Heartseeker:
      total: 0.52
      efficiency: 0.47
      win: 0.54
      pick: 0.45
      fit: 0.6
    The Crusher:
      total: 0.58
      efficiency: 0.47
      win: 0.75
      pick: 0.32
      fit: 0.43
    Titan's Bane:
      total: 0.55
      efficiency: 0.47
      win: 0.67
      pick: 0.35
      fit: 0.43
  community_ordered:
  - Transcendence
  - Jotunn's Revenge
  - Heartseeker
  - The Crusher
  - Titan's Bane
  starter: *id001
  aspect: Aspect of the Heroic Tutor
- source: suggested
  archetype: crit
  slot_order:
  - Jotunn's Revenge
  - Musashi's Dual Swords
  - Demon Blade
  - The Crusher
  - Deathbringer
  - Titan's Bane
  flex_slots:
  - Demon Blade
  - Musashi's Dual Swords
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Crit / auto-attack skew (efficiency + fit + win/pick). Underrated for
    this god: Riptalon, The Reaper, Silverbranch Bow, Tekko-Kagi, Lernaean Bow, Hydra''s
    Lament, Deathbringer, Demon Blade, Golden Blade, Dominance, Musashi''s Dual Swords,
    Toxic Blade, Tyrfing, Arondight, Damaru, Rage, Pendulum Blade, Qin''s Blade, Runeforged
    Hammer, Berserker''s Shield, Avenging Blade, Barbed Carver, Sun Beam Bow, Bloodforge.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.64
      efficiency: 0.72
      win: 0.63
      pick: 0.97
      fit: 0.41
    Musashi's Dual Swords:
      total: 0.48
      efficiency: 0.46
      win: 0.57
      pick: 0.0
      fit: 0.42
    Demon Blade:
      total: 0.49
      efficiency: 0.38
      win: 0.57
      pick: 0.0
      fit: 0.64
    The Crusher:
      total: 0.58
      efficiency: 0.47
      win: 0.75
      pick: 0.32
      fit: 0.42
    Deathbringer:
      total: 0.5
      efficiency: 0.51
      win: 0.57
      pick: 0.0
      fit: 0.42
    Titan's Bane:
      total: 0.55
      efficiency: 0.47
      win: 0.67
      pick: 0.35
      fit: 0.42
  community_ordered:
  - Jotunn's Revenge
  - The Crusher
  - Titan's Bane
  starter: *id001
  aspect: Aspect of the Heroic Tutor
- source: suggested
  archetype: burst
  slot_order:
  - Transcendence
  - Jotunn's Revenge
  - The Reaper
  - Heartseeker
  - The Crusher
  - Titan's Bane
  flex_slots:
  - Heartseeker
  - Transcendence
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
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: The Reaper, Hydra''s Lament, Riptalon, Tekko-Kagi, Silverbranch Bow, Deathbringer,
    Pendulum Blade, Lernaean Bow, Arondight, Musashi''s Dual Swords, Runeforged Hammer,
    Toxic Blade, Golden Blade, Dominance, Damaru, Rage, Demon Blade, Tyrfing, Avenging
    Blade, Barbed Carver, Breastplate of Valor, Genji''s Guard, Daybreak Gavel, Bloodforge.'
  slot_scores:
    Transcendence:
      total: 0.52
      efficiency: 0.53
      win: 0.6
      pick: 0.78
      fit: 0.15
    Jotunn's Revenge:
      total: 0.66
      efficiency: 0.72
      win: 0.63
      pick: 0.97
      fit: 0.53
    The Reaper:
      total: 0.52
      efficiency: 0.55
      win: 0.57
      pick: 0.0
      fit: 0.45
    Heartseeker:
      total: 0.52
      efficiency: 0.47
      win: 0.54
      pick: 0.45
      fit: 0.58
    The Crusher:
      total: 0.59
      efficiency: 0.47
      win: 0.75
      pick: 0.32
      fit: 0.48
    Titan's Bane:
      total: 0.56
      efficiency: 0.47
      win: 0.67
      pick: 0.35
      fit: 0.48
  community_ordered:
  - Transcendence
  - Jotunn's Revenge
  - Heartseeker
  - The Crusher
  - Titan's Bane
  starter: *id001
  aspect: Aspect of the Heroic Tutor
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - The Reaper
  - The Crusher
  - Titan's Bane
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Titan's Bane
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, The Reaper, Berserker''s Shield, Shield of the Phoenix,
    Riptalon, Kinetic Cuirass, Freya''s Tears, Genji''s Guard, Breastplate of Valor,
    Runeforged Hammer, Erosion, Shifter''s Shield, Yogi''s Necklace, Shield Splitter,
    Pharaoh''s Curse, Eye of the Storm, Umbral Link, Golden Blade, Phoenix Feather,
    Hydra''s Lament, Shogun''s Ofuda, Eye of Providence, Void Shield, Stampede, Draconic
    Scale, Daybreak Gavel, Avenging Blade, Chandra''s Grace.'
  slot_scores:
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.57
      pick: 0.0
      fit: 0.3
    Jotunn's Revenge:
      total: 0.63
      efficiency: 0.72
      win: 0.63
      pick: 0.97
      fit: 0.34
    The Reaper:
      total: 0.54
      efficiency: 0.55
      win: 0.57
      pick: 0.0
      fit: 0.63
    The Crusher:
      total: 0.57
      efficiency: 0.47
      win: 0.75
      pick: 0.32
      fit: 0.36
    Titan's Bane:
      total: 0.54
      efficiency: 0.47
      win: 0.67
      pick: 0.35
      fit: 0.36
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.77
  community_ordered:
  - Jotunn's Revenge
  - The Crusher
  - Titan's Bane
  starter: *id001
  aspect: Aspect of the Heroic Tutor
- source: suggested
  archetype: anti-tank
  slot_order:
  - Transcendence
  - Jotunn's Revenge
  - The Reaper
  - Heartseeker
  - The Crusher
  - Titan's Bane
  flex_slots:
  - Heartseeker
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: The Reaper, Riptalon, Tekko-Kagi, Silverbranch Bow, Hydra''s Lament,
    Pendulum Blade, Avenging Blade, Deathbringer, Lernaean Bow, Toxic Blade, Musashi''s
    Dual Swords, Arondight, Oath-Sworn Spear, Damaru, Rage, Golden Blade, Runeforged
    Hammer, Dominance, Demon Blade, Tyrfing, Barbed Carver, The Executioner, Screeching
    Gargoyle, Bloodforge.'
  slot_scores:
    Transcendence:
      total: 0.52
      efficiency: 0.53
      win: 0.6
      pick: 0.78
      fit: 0.17
    Jotunn's Revenge:
      total: 0.68
      efficiency: 0.72
      win: 0.63
      pick: 0.97
      fit: 0.62
    The Reaper:
      total: 0.54
      efficiency: 0.55
      win: 0.57
      pick: 0.0
      fit: 0.62
    Heartseeker:
      total: 0.54
      efficiency: 0.47
      win: 0.54
      pick: 0.45
      fit: 0.73
    The Crusher:
      total: 0.61
      efficiency: 0.47
      win: 0.75
      pick: 0.32
      fit: 0.63
    Titan's Bane:
      total: 0.58
      efficiency: 0.47
      win: 0.67
      pick: 0.35
      fit: 0.63
  community_ordered:
  - Transcendence
  - Jotunn's Revenge
  - Heartseeker
  - The Crusher
  - Titan's Bane
  starter: *id001
  aspect: Aspect of the Heroic Tutor
- source: suggested
  archetype: attack-speed
  slot_order:
  - Lernaean Bow
  - Jotunn's Revenge
  - Riptalon
  - The Crusher
  - Silverbranch Bow
  - Titan's Bane
  flex_slots:
  - Silverbranch Bow
  - Lernaean Bow
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Riptalon, Silverbranch Bow, Lernaean Bow, Tekko-Kagi, The Reaper, Golden
    Blade, Hydra''s Lament, Toxic Blade, Tyrfing, Deathbringer, Dominance, Qin''s
    Blade, Demon Blade, Musashi''s Dual Swords, Arondight, Sun Beam Bow, Pendulum
    Blade, Runeforged Hammer, Berserker''s Shield, Damaru, Rage, Avenging Blade, Dagger
    of Frenzy, Barbed Carver.'
  slot_scores:
    Lernaean Bow:
      total: 0.5
      efficiency: 0.52
      win: 0.57
      pick: 0.0
      fit: 0.45
    Jotunn's Revenge:
      total: 0.63
      efficiency: 0.72
      win: 0.63
      pick: 0.97
      fit: 0.35
    Riptalon:
      total: 0.52
      efficiency: 0.51
      win: 0.57
      pick: 0.0
      fit: 0.6
    The Crusher:
      total: 0.57
      efficiency: 0.47
      win: 0.75
      pick: 0.32
      fit: 0.36
    Silverbranch Bow:
      total: 0.52
      efficiency: 0.53
      win: 0.57
      pick: 0.0
      fit: 0.52
    Titan's Bane:
      total: 0.54
      efficiency: 0.47
      win: 0.67
      pick: 0.35
      fit: 0.36
  community_ordered:
  - Jotunn's Revenge
  - The Crusher
  - Titan's Bane
  starter: *id001
  aspect: Aspect of the Heroic Tutor
- source: suggested
  archetype: cooldown
  slot_order:
  - Transcendence
  - Jotunn's Revenge
  - Hydra's Lament
  - The Crusher
  - Arondight
  - Titan's Bane
  flex_slots:
  - Transcendence
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
    + fit + win/pick). Underrated for this god: Hydra''s Lament, The Reaper, Arondight,
    Pendulum Blade, Riptalon, Deathbringer, Silverbranch Bow, Lernaean Bow, Tekko-Kagi,
    Breastplate of Valor, Musashi''s Dual Swords, Genji''s Guard, Runeforged Hammer,
    Golden Blade, Damaru, Rage, Dominance, Toxic Blade, Demon Blade, Tyrfing, Avenging
    Blade, Eye of Erebus, Daybreak Gavel, Barbed Carver.'
  slot_scores:
    Transcendence:
      total: 0.51
      efficiency: 0.53
      win: 0.6
      pick: 0.78
      fit: 0.1
    Jotunn's Revenge:
      total: 0.67
      efficiency: 0.72
      win: 0.63
      pick: 0.97
      fit: 0.57
    Hydra's Lament:
      total: 0.52
      efficiency: 0.54
      win: 0.57
      pick: 0.0
      fit: 0.52
    The Crusher:
      total: 0.57
      efficiency: 0.47
      win: 0.75
      pick: 0.32
      fit: 0.35
    Arondight:
      total: 0.49
      efficiency: 0.5
      win: 0.57
      pick: 0.0
      fit: 0.42
    Titan's Bane:
      total: 0.54
      efficiency: 0.47
      win: 0.67
      pick: 0.35
      fit: 0.35
  community_ordered:
  - Transcendence
  - Jotunn's Revenge
  - The Crusher
  - Titan's Bane
  starter: *id001
  aspect: Aspect of the Heroic Tutor
- source: suggested
  archetype: model
  slot_order:
  - Transcendence
  - Jotunn's Revenge
  - Hydra's Lament
  - Heartseeker
  - The Reaper
  - Deathbringer
  flex_slots:
  - Deathbringer
  - Transcendence
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
    Underrated for this god: The Reaper, Hydra''s Lament, Deathbringer, Riptalon,
    Tekko-Kagi, Silverbranch Bow, Tyrfing, Lernaean Bow, Musashi''s Dual Swords, Pendulum
    Blade, Arondight, Damaru, Rage, Demon Blade, Golden Blade, Dominance, Runeforged
    Hammer, Toxic Blade, Barbed Carver, Avenging Blade, Bloodforge, Qin''s Blade,
    Shield Splitter, Breastplate of Valor.'
  slot_scores:
    Transcendence:
      total: 0.52
      efficiency: 0.53
      win: 0.6
      pick: 0.78
      fit: 0.2
    Jotunn's Revenge:
      total: 0.66
      efficiency: 0.72
      win: 0.63
      pick: 0.97
      fit: 0.53
    Hydra's Lament:
      total: 0.51
      efficiency: 0.54
      win: 0.57
      pick: 0.0
      fit: 0.42
    Heartseeker:
      total: 0.52
      efficiency: 0.47
      win: 0.54
      pick: 0.45
      fit: 0.61
    The Reaper:
      total: 0.53
      efficiency: 0.55
      win: 0.57
      pick: 0.0
      fit: 0.53
    Deathbringer:
      total: 0.51
      efficiency: 0.51
      win: 0.57
      pick: 0.0
      fit: 0.49
  community_ordered:
  - Transcendence
  - Jotunn's Revenge
  - Heartseeker
  starter: *id001
  aspect: Aspect of the Heroic Tutor
---
