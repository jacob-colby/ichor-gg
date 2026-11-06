---
type: smite-build
god: Chiron
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Heroic Tutor
  aspect_pick_rate: 0.01
  aspect_win_rate: 0.5
  slot_order:
  - name: Transcendence
    pick_rate: 0.79
    win_rate: 0.56
    alternates:
    - name: Devourer's Gauntlet
      pick_rate: 0.12
      win_rate: 0.69
    - name: Jotunn's Revenge
      pick_rate: 0.04
      win_rate: 0.33
  - name: Jotunn's Revenge
    pick_rate: 0.63
    win_rate: 0.56
    alternates:
    - name: Transcendence
      pick_rate: 0.07
      win_rate: 0.44
    - name: Dagger of Frenzy
      pick_rate: 0.06
      win_rate: 0.5
  - name: The Crusher
    pick_rate: 0.34
    win_rate: 0.5
    alternates:
    - name: Heartseeker
      pick_rate: 0.21
      win_rate: 0.61
    - name: Avatar's Parashu
      pick_rate: 0.11
      win_rate: 0.57
  - name: Heartseeker
    pick_rate: 0.38
    win_rate: 0.61
    alternates:
    - name: The Crusher
      pick_rate: 0.14
      win_rate: 0.72
    - name: Avatar's Parashu
      pick_rate: 0.13
      win_rate: 0.41
  - name: Titan's Bane
    pick_rate: 0.14
    win_rate: 0.81
    alternates:
    - name: The Crusher
      pick_rate: 0.14
      win_rate: 0.63
    - name: Avatar's Parashu
      pick_rate: 0.13
      win_rate: 0.73
  - name: Skeggox
    pick_rate: 0.15
    win_rate: 0.55
    alternates:
    - name: Titan's Bane
      pick_rate: 0.09
      win_rate: 0.43
    - name: Avatar's Parashu
      pick_rate: 0.09
      win_rate: 0.57
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.34
    win_rate: 0.67
  - name: Bluestone Pendant
    pick_rate: 0.18
    win_rate: 0.6
  - name: Pendulum of the Ages
    pick_rate: 0.15
    win_rate: 0.48
  source_url: https://smitebrain.com/gods/chiron/
  last_verified: '2026-11-06'
  god_win_rate: 0.5735294117647058
  god_matches_won: 78
  god_matches_played: 136
  god_division: obsidian
  god_window_start: '2026-11-03'
  god_window_end: '2026-11-06'
  god_matches_analyzed: 2859
  starter:
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: core
  slot_order:
  - Transcendence
  - Jotunn's Revenge
  - Tyrfing
  - Heartseeker
  - Avatar's Parashu
  - Titan's Bane
  flex_slots:
  - Tyrfing
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Tyrfing, The Reaper, Tekko-Kagi, Hydra''s Lament, Lernaean Bow, Dominance,
    Silverbranch Bow, Riptalon, Golden Blade, Arondight, Demon Blade, Toxic Blade,
    Rage, Deathbringer, Qin''s Blade, Pendulum Blade, Bloodforge, Runeforged Hammer,
    Berserker''s Shield, Barbed Carver, Musashi''s Dual Swords, Damaru, Genji''s Guard,
    Dagger of Frenzy.'
  slot_scores:
    Transcendence:
      total: 0.49
      efficiency: 0.5
      win: 0.56
      pick: 0.79
      fit: 0.17
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.65
      win: 0.56
      pick: 0.86
      fit: 0.44
    Tyrfing:
      total: 0.52
      efficiency: 0.53
      win: 0.56
      pick: 0.0
      fit: 0.57
    Heartseeker:
      total: 0.55
      efficiency: 0.45
      win: 0.61
      pick: 0.63
      fit: 0.54
    Avatar's Parashu:
      total: 0.55
      efficiency: 0.46
      win: 0.73
      pick: 0.28
      fit: 0.34
    Titan's Bane:
      total: 0.61
      efficiency: 0.48
      win: 0.81
      pick: 0.3
      fit: 0.44
  community_ordered:
  - Transcendence
  - Jotunn's Revenge
  - Heartseeker
  - Avatar's Parashu
  - Titan's Bane
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: mana-stack
  slot_order:
  - Transcendence
  - Jotunn's Revenge
  - Tyrfing
  - Heartseeker
  - Avatar's Parashu
  - Titan's Bane
  flex_slots:
  - Tyrfing
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Tyrfing,
    Hydra''s Lament, The Reaper, Dominance, Tekko-Kagi, Lernaean Bow, Arondight, Silverbranch
    Bow, Golden Blade, Riptalon, Rage, Deathbringer, Demon Blade, Genji''s Guard,
    Toxic Blade, Runeforged Hammer, Qin''s Blade, Bloodforge, Barbed Carver, Pendulum
    Blade, Damaru, Shield Splitter, Eye of the Storm, Avenging Blade.'
  slot_scores:
    Transcendence:
      total: 0.5
      efficiency: 0.5
      win: 0.56
      pick: 0.79
      fit: 0.24
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.65
      win: 0.56
      pick: 0.86
      fit: 0.44
    Tyrfing:
      total: 0.51
      efficiency: 0.53
      win: 0.56
      pick: 0.0
      fit: 0.48
    Heartseeker:
      total: 0.55
      efficiency: 0.45
      win: 0.61
      pick: 0.63
      fit: 0.55
    Avatar's Parashu:
      total: 0.55
      efficiency: 0.46
      win: 0.73
      pick: 0.28
      fit: 0.29
    Titan's Bane:
      total: 0.61
      efficiency: 0.48
      win: 0.81
      pick: 0.3
      fit: 0.39
  community_ordered:
  - Transcendence
  - Jotunn's Revenge
  - Heartseeker
  - Avatar's Parashu
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: crit
  slot_order:
  - Rage
  - Jotunn's Revenge
  - Demon Blade
  - Avatar's Parashu
  - Titan's Bane
  - Deathbringer
  flex_slots:
  - Demon Blade
  - Deathbringer
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    this god: Tyrfing, The Reaper, Tekko-Kagi, Hydra''s Lament, Silverbranch Bow,
    Riptalon, Lernaean Bow, Dominance, Rage, Demon Blade, Golden Blade, Arondight,
    Toxic Blade, Deathbringer, Qin''s Blade, Pendulum Blade, Bloodforge, Berserker''s
    Shield, Musashi''s Dual Swords, Runeforged Hammer, Barbed Carver, Damaru, Genji''s
    Guard, Dagger of Frenzy.'
  slot_scores:
    Rage:
      total: 0.48
      efficiency: 0.46
      win: 0.56
      pick: 0.0
      fit: 0.42
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.65
      win: 0.56
      pick: 0.86
      fit: 0.41
    Demon Blade:
      total: 0.48
      efficiency: 0.36
      win: 0.56
      pick: 0.0
      fit: 0.64
    Avatar's Parashu:
      total: 0.55
      efficiency: 0.46
      win: 0.73
      pick: 0.28
      fit: 0.32
    Titan's Bane:
      total: 0.61
      efficiency: 0.48
      win: 0.81
      pick: 0.3
      fit: 0.42
    Deathbringer:
      total: 0.47
      efficiency: 0.44
      win: 0.56
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Jotunn's Revenge
  - Avatar's Parashu
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Transcendence
  - Jotunn's Revenge
  - The Reaper
  - Heartseeker
  - Avatar's Parashu
  - Titan's Bane
  flex_slots:
  - The Reaper
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    god: The Reaper, Tyrfing, Hydra''s Lament, Tekko-Kagi, Silverbranch Bow, Riptalon,
    Lernaean Bow, Dominance, Arondight, Toxic Blade, Golden Blade, Rage, Pendulum
    Blade, Deathbringer, Qin''s Blade, Demon Blade, Damaru, Genji''s Guard, Runeforged
    Hammer, Bloodforge, Barbed Carver, Berserker''s Shield, Shield Splitter, Dagger
    of Frenzy.'
  slot_scores:
    Transcendence:
      total: 0.49
      efficiency: 0.5
      win: 0.56
      pick: 0.79
      fit: 0.13
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.65
      win: 0.56
      pick: 0.86
      fit: 0.46
    The Reaper:
      total: 0.51
      efficiency: 0.57
      win: 0.56
      pick: 0.0
      fit: 0.39
    Heartseeker:
      total: 0.54
      efficiency: 0.45
      win: 0.61
      pick: 0.63
      fit: 0.53
    Avatar's Parashu:
      total: 0.55
      efficiency: 0.46
      win: 0.73
      pick: 0.28
      fit: 0.33
    Titan's Bane:
      total: 0.61
      efficiency: 0.48
      win: 0.81
      pick: 0.3
      fit: 0.43
  community_ordered:
  - Transcendence
  - Jotunn's Revenge
  - Heartseeker
  - Avatar's Parashu
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - The Reaper
  - Avatar's Parashu
  - Titan's Bane
  - Amanita Charm
  flex_slots:
  - The Reaper
  - Avatar's Parashu
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
    this god: Amanita Charm, Berserker''s Shield, The Reaper, Shield of the Phoenix,
    Kinetic Cuirass, Genji''s Guard, Yogi''s Necklace, Riptalon, Phoenix Feather,
    Freya''s Tears, Tyrfing, Shield Splitter, Breastplate of Valor, Chandra''s Grace,
    Golden Blade, Runeforged Hammer, Oni Hunter''s Garb, Hydra''s Lament, Draconic
    Scale, Regrowth Striders, Bloodforge, Tekko-Kagi, Toxic Blade, Shogun''s Ofuda,
    Erosion, Pharaoh''s Curse, Midgardian Mail, Eye of Providence.'
  slot_scores:
    Berserker's Shield:
      total: 0.56
      efficiency: 0.72
      win: 0.56
      pick: 0.0
      fit: 0.38
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.65
      win: 0.56
      pick: 0.86
      fit: 0.3
    The Reaper:
      total: 0.54
      efficiency: 0.57
      win: 0.56
      pick: 0.0
      fit: 0.59
    Avatar's Parashu:
      total: 0.54
      efficiency: 0.46
      win: 0.73
      pick: 0.28
      fit: 0.23
    Titan's Bane:
      total: 0.6
      efficiency: 0.48
      win: 0.81
      pick: 0.3
      fit: 0.33
    Amanita Charm:
      total: 0.58
      efficiency: 0.68
      win: 0.56
      pick: 0.0
      fit: 0.62
  community_ordered:
  - Jotunn's Revenge
  - Avatar's Parashu
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Transcendence
  - Jotunn's Revenge
  - The Reaper
  - Heartseeker
  - Avatar's Parashu
  - Titan's Bane
  flex_slots:
  - The Reaper
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    for this god: The Reaper, Tekko-Kagi, Tyrfing, Silverbranch Bow, Riptalon, Hydra''s
    Lament, Toxic Blade, Lernaean Bow, Dominance, Avenging Blade, Arondight, Pendulum
    Blade, Golden Blade, Rage, Demon Blade, Deathbringer, Qin''s Blade, Oath-Sworn
    Spear, The Executioner, Runeforged Hammer, Bloodforge, Berserker''s Shield, Screeching
    Gargoyle, Barbed Carver.'
  slot_scores:
    Transcendence:
      total: 0.49
      efficiency: 0.5
      win: 0.56
      pick: 0.79
      fit: 0.14
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.65
      win: 0.56
      pick: 0.86
      fit: 0.53
    The Reaper:
      total: 0.53
      efficiency: 0.57
      win: 0.56
      pick: 0.0
      fit: 0.52
    Heartseeker:
      total: 0.56
      efficiency: 0.45
      win: 0.61
      pick: 0.63
      fit: 0.65
    Avatar's Parashu:
      total: 0.57
      efficiency: 0.46
      win: 0.73
      pick: 0.28
      fit: 0.45
    Titan's Bane:
      total: 0.63
      efficiency: 0.48
      win: 0.81
      pick: 0.3
      fit: 0.55
  community_ordered:
  - Transcendence
  - Jotunn's Revenge
  - Heartseeker
  - Avatar's Parashu
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - The Reaper
  - Riptalon
  - Silverbranch Bow
  - Titan's Bane
  flex_slots:
  - Silverbranch Bow
  - Riptalon
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
    this god: Tyrfing, The Reaper, Silverbranch Bow, Riptalon, Tekko-Kagi, Hydra''s
    Lament, Lernaean Bow, Dominance, Golden Blade, Toxic Blade, Qin''s Blade, Arondight,
    Rage, Demon Blade, Deathbringer, Berserker''s Shield, Runeforged Hammer, Bloodforge,
    Damaru, Genji''s Guard, Pendulum Blade, Barbed Carver, Sun Beam Bow, Dagger of
    Frenzy.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.65
      win: 0.56
      pick: 0.86
      fit: 0.35
    Tyrfing:
      total: 0.53
      efficiency: 0.53
      win: 0.56
      pick: 0.0
      fit: 0.6
    The Reaper:
      total: 0.5
      efficiency: 0.57
      win: 0.56
      pick: 0.0
      fit: 0.34
    Riptalon:
      total: 0.5
      efficiency: 0.45
      win: 0.56
      pick: 0.0
      fit: 0.6
    Silverbranch Bow:
      total: 0.5
      efficiency: 0.49
      win: 0.56
      pick: 0.0
      fit: 0.52
    Titan's Bane:
      total: 0.6
      efficiency: 0.48
      win: 0.81
      pick: 0.3
      fit: 0.36
  community_ordered:
  - Jotunn's Revenge
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Arondight
  - Heartseeker
  - Avatar's Parashu
  - Titan's Bane
  flex_slots:
  - Hydra's Lament
  - Arondight
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    + fit + win/pick). Underrated for this god: Hydra''s Lament, Tyrfing, The Reaper,
    Arondight, Tekko-Kagi, Silverbranch Bow, Lernaean Bow, Dominance, Riptalon, Damaru,
    Genji''s Guard, Pendulum Blade, Toxic Blade, Golden Blade, Qin''s Blade, Rage,
    Breastplate of Valor, Chandra''s Grace, Deathbringer, Demon Blade, Berserker''s
    Shield, Runeforged Hammer, Bloodforge, Dagger of Frenzy.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.65
      win: 0.56
      pick: 0.86
      fit: 0.49
    Hydra's Lament:
      total: 0.51
      efficiency: 0.55
      win: 0.56
      pick: 0.0
      fit: 0.46
    Arondight:
      total: 0.49
      efficiency: 0.53
      win: 0.56
      pick: 0.0
      fit: 0.36
    Heartseeker:
      total: 0.53
      efficiency: 0.45
      win: 0.61
      pick: 0.63
      fit: 0.41
    Avatar's Parashu:
      total: 0.54
      efficiency: 0.46
      win: 0.73
      pick: 0.28
      fit: 0.21
    Titan's Bane:
      total: 0.59
      efficiency: 0.48
      win: 0.81
      pick: 0.3
      fit: 0.31
  community_ordered:
  - Jotunn's Revenge
  - Heartseeker
  - Avatar's Parashu
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Transcendence
  - Jotunn's Revenge
  - Tyrfing
  - Hydra's Lament
  - The Reaper
  - Tekko-Kagi
  flex_slots:
  - Hydra's Lament
  - Transcendence
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
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Tyrfing, The Reaper, Tekko-Kagi, Hydra''s Lament, Lernaean
    Bow, Dominance, Silverbranch Bow, Riptalon, Golden Blade, Arondight, Demon Blade,
    Toxic Blade, Rage, Deathbringer, Qin''s Blade, Pendulum Blade, Bloodforge, Runeforged
    Hammer, Berserker''s Shield, Barbed Carver, Dagger of Frenzy, Musashi''s Dual
    Swords, Damaru, Genji''s Guard.'
  slot_scores:
    Transcendence:
      total: 0.49
      efficiency: 0.5
      win: 0.56
      pick: 0.79
      fit: 0.17
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.65
      win: 0.56
      pick: 0.86
      fit: 0.44
    Tyrfing:
      total: 0.52
      efficiency: 0.53
      win: 0.56
      pick: 0.0
      fit: 0.57
    Hydra's Lament:
      total: 0.5
      efficiency: 0.55
      win: 0.56
      pick: 0.0
      fit: 0.36
    The Reaper:
      total: 0.52
      efficiency: 0.57
      win: 0.56
      pick: 0.0
      fit: 0.43
    Tekko-Kagi:
      total: 0.51
      efficiency: 0.49
      win: 0.56
      pick: 0.0
      fit: 0.58
  community_ordered:
  - Transcendence
  - Jotunn's Revenge
  starter: *id001
- source: suggested
  archetype: core
  slot_order:
  - Transcendence
  - Jotunn's Revenge
  - The Reaper
  - Heartseeker
  - Avatar's Parashu
  - Titan's Bane
  flex_slots:
  - The Reaper
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: The Reaper, Hydra''s Lament, Tyrfing, Tekko-Kagi, Rage, Arondight, Deathbringer,
    Riptalon, Silverbranch Bow, Lernaean Bow, Dominance, Pendulum Blade, Demon Blade,
    Golden Blade, Bloodforge, Musashi''s Dual Swords, Barbed Carver, Toxic Blade,
    Runeforged Hammer, Damaru, Genji''s Guard, Shield Splitter, Eye of the Storm,
    Avenging Blade.'
  slot_scores:
    Transcendence:
      total: 0.5
      efficiency: 0.5
      win: 0.56
      pick: 0.79
      fit: 0.2
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.65
      win: 0.56
      pick: 0.86
      fit: 0.53
    The Reaper:
      total: 0.53
      efficiency: 0.57
      win: 0.56
      pick: 0.0
      fit: 0.53
    Heartseeker:
      total: 0.56
      efficiency: 0.45
      win: 0.61
      pick: 0.63
      fit: 0.61
    Avatar's Parashu:
      total: 0.57
      efficiency: 0.46
      win: 0.73
      pick: 0.28
      fit: 0.41
    Titan's Bane:
      total: 0.62
      efficiency: 0.48
      win: 0.81
      pick: 0.3
      fit: 0.51
  community_ordered:
  - Transcendence
  - Jotunn's Revenge
  - Heartseeker
  - Avatar's Parashu
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
  - Avatar's Parashu
  - Titan's Bane
  flex_slots:
  - Hydra's Lament
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Hydra''s
    Lament, The Reaper, Tyrfing, Arondight, Dominance, Tekko-Kagi, Rage, Lernaean
    Bow, Deathbringer, Genji''s Guard, Silverbranch Bow, Runeforged Hammer, Pendulum
    Blade, Golden Blade, Bloodforge, Riptalon, Barbed Carver, Damaru, Shield Splitter,
    Demon Blade, Eye of the Storm, Avenging Blade, Musashi''s Dual Swords, Toxic Blade.'
  slot_scores:
    Transcendence:
      total: 0.51
      efficiency: 0.5
      win: 0.56
      pick: 0.79
      fit: 0.27
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.65
      win: 0.56
      pick: 0.86
      fit: 0.5
    Hydra's Lament:
      total: 0.52
      efficiency: 0.55
      win: 0.56
      pick: 0.0
      fit: 0.47
    Heartseeker:
      total: 0.55
      efficiency: 0.45
      win: 0.61
      pick: 0.63
      fit: 0.6
    Avatar's Parashu:
      total: 0.55
      efficiency: 0.46
      win: 0.73
      pick: 0.28
      fit: 0.33
    Titan's Bane:
      total: 0.61
      efficiency: 0.48
      win: 0.81
      pick: 0.3
      fit: 0.43
  community_ordered:
  - Transcendence
  - Jotunn's Revenge
  - Heartseeker
  - Avatar's Parashu
  - Titan's Bane
  starter: *id001
  aspect: Aspect of the Heroic Tutor
- source: suggested
  archetype: crit
  slot_order:
  - Rage
  - Jotunn's Revenge
  - Demon Blade
  - Avatar's Parashu
  - Titan's Bane
  - Deathbringer
  flex_slots:
  - Demon Blade
  - Deathbringer
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    this god: Tyrfing, The Reaper, Tekko-Kagi, Hydra''s Lament, Silverbranch Bow,
    Riptalon, Lernaean Bow, Dominance, Rage, Demon Blade, Golden Blade, Arondight,
    Toxic Blade, Deathbringer, Qin''s Blade, Pendulum Blade, Bloodforge, Berserker''s
    Shield, Musashi''s Dual Swords, Runeforged Hammer, Barbed Carver, Damaru, Genji''s
    Guard, Dagger of Frenzy.'
  slot_scores:
    Rage:
      total: 0.48
      efficiency: 0.46
      win: 0.56
      pick: 0.0
      fit: 0.42
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.65
      win: 0.56
      pick: 0.86
      fit: 0.41
    Demon Blade:
      total: 0.48
      efficiency: 0.36
      win: 0.56
      pick: 0.0
      fit: 0.64
    Avatar's Parashu:
      total: 0.55
      efficiency: 0.46
      win: 0.73
      pick: 0.28
      fit: 0.32
    Titan's Bane:
      total: 0.61
      efficiency: 0.48
      win: 0.81
      pick: 0.3
      fit: 0.42
    Deathbringer:
      total: 0.47
      efficiency: 0.44
      win: 0.56
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Jotunn's Revenge
  - Avatar's Parashu
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
  - Avatar's Parashu
  - Titan's Bane
  flex_slots:
  - The Reaper
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: The Reaper, Hydra''s Lament, Tyrfing, Tekko-Kagi, Arondight, Silverbranch
    Bow, Pendulum Blade, Riptalon, Rage, Lernaean Bow, Dominance, Deathbringer, Toxic
    Blade, Damaru, Genji''s Guard, Runeforged Hammer, Golden Blade, Bloodforge, Barbed
    Carver, Demon Blade, Shield Splitter, Musashi''s Dual Swords, Eye of the Storm,
    Avenging Blade.'
  slot_scores:
    Transcendence:
      total: 0.49
      efficiency: 0.5
      win: 0.56
      pick: 0.79
      fit: 0.15
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.65
      win: 0.56
      pick: 0.86
      fit: 0.53
    The Reaper:
      total: 0.52
      efficiency: 0.57
      win: 0.56
      pick: 0.0
      fit: 0.45
    Heartseeker:
      total: 0.55
      efficiency: 0.45
      win: 0.61
      pick: 0.63
      fit: 0.58
    Avatar's Parashu:
      total: 0.56
      efficiency: 0.46
      win: 0.73
      pick: 0.28
      fit: 0.38
    Titan's Bane:
      total: 0.62
      efficiency: 0.48
      win: 0.81
      pick: 0.3
      fit: 0.48
  community_ordered:
  - Transcendence
  - Jotunn's Revenge
  - Heartseeker
  - Avatar's Parashu
  - Titan's Bane
  starter: *id001
  aspect: Aspect of the Heroic Tutor
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - The Reaper
  - Avatar's Parashu
  - Titan's Bane
  - Amanita Charm
  flex_slots:
  - The Reaper
  - Avatar's Parashu
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
    this god: Amanita Charm, Berserker''s Shield, The Reaper, Shield of the Phoenix,
    Kinetic Cuirass, Genji''s Guard, Phoenix Feather, Yogi''s Necklace, Freya''s Tears,
    Shield Splitter, Breastplate of Valor, Erosion, Chandra''s Grace, Runeforged Hammer,
    Riptalon, Oni Hunter''s Garb, Draconic Scale, Hydra''s Lament, Regrowth Striders,
    Bloodforge, Tyrfing, Umbral Link, Eye of Providence, Midgardian Mail, Void Stone,
    Golden Blade, Stampede, Shogun''s Ofuda.'
  slot_scores:
    Berserker's Shield:
      total: 0.55
      efficiency: 0.72
      win: 0.56
      pick: 0.0
      fit: 0.3
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.65
      win: 0.56
      pick: 0.86
      fit: 0.34
    The Reaper:
      total: 0.55
      efficiency: 0.57
      win: 0.56
      pick: 0.0
      fit: 0.63
    Avatar's Parashu:
      total: 0.54
      efficiency: 0.46
      win: 0.73
      pick: 0.28
      fit: 0.26
    Titan's Bane:
      total: 0.6
      efficiency: 0.48
      win: 0.81
      pick: 0.3
      fit: 0.36
    Amanita Charm:
      total: 0.61
      efficiency: 0.68
      win: 0.56
      pick: 0.0
      fit: 0.77
  community_ordered:
  - Jotunn's Revenge
  - Avatar's Parashu
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
  - Avatar's Parashu
  - Titan's Bane
  flex_slots:
  - The Reaper
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: The Reaper, Tekko-Kagi, Hydra''s Lament, Tyrfing, Silverbranch Bow,
    Riptalon, Pendulum Blade, Avenging Blade, Toxic Blade, Arondight, Rage, Deathbringer,
    Lernaean Bow, Dominance, Golden Blade, Oath-Sworn Spear, Bloodforge, Runeforged
    Hammer, Barbed Carver, Demon Blade, Screeching Gargoyle, Damaru, Genji''s Guard,
    Musashi''s Dual Swords.'
  slot_scores:
    Transcendence:
      total: 0.49
      efficiency: 0.5
      win: 0.56
      pick: 0.79
      fit: 0.17
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.65
      win: 0.56
      pick: 0.86
      fit: 0.62
    The Reaper:
      total: 0.54
      efficiency: 0.57
      win: 0.56
      pick: 0.0
      fit: 0.62
    Heartseeker:
      total: 0.57
      efficiency: 0.45
      win: 0.61
      pick: 0.63
      fit: 0.73
    Avatar's Parashu:
      total: 0.58
      efficiency: 0.46
      win: 0.73
      pick: 0.28
      fit: 0.53
    Titan's Bane:
      total: 0.64
      efficiency: 0.48
      win: 0.81
      pick: 0.3
      fit: 0.63
  community_ordered:
  - Transcendence
  - Jotunn's Revenge
  - Heartseeker
  - Avatar's Parashu
  - Titan's Bane
  starter: *id001
  aspect: Aspect of the Heroic Tutor
- source: suggested
  archetype: attack-speed
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - The Reaper
  - Riptalon
  - Silverbranch Bow
  - Titan's Bane
  flex_slots:
  - Silverbranch Bow
  - Riptalon
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
    this god: Tyrfing, The Reaper, Silverbranch Bow, Riptalon, Tekko-Kagi, Hydra''s
    Lament, Lernaean Bow, Dominance, Golden Blade, Toxic Blade, Qin''s Blade, Arondight,
    Rage, Demon Blade, Deathbringer, Berserker''s Shield, Runeforged Hammer, Bloodforge,
    Damaru, Genji''s Guard, Pendulum Blade, Barbed Carver, Sun Beam Bow, Dagger of
    Frenzy.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.65
      win: 0.56
      pick: 0.86
      fit: 0.35
    Tyrfing:
      total: 0.53
      efficiency: 0.53
      win: 0.56
      pick: 0.0
      fit: 0.6
    The Reaper:
      total: 0.5
      efficiency: 0.57
      win: 0.56
      pick: 0.0
      fit: 0.34
    Riptalon:
      total: 0.5
      efficiency: 0.45
      win: 0.56
      pick: 0.0
      fit: 0.6
    Silverbranch Bow:
      total: 0.5
      efficiency: 0.49
      win: 0.56
      pick: 0.0
      fit: 0.52
    Titan's Bane:
      total: 0.6
      efficiency: 0.48
      win: 0.81
      pick: 0.3
      fit: 0.36
  community_ordered:
  - Jotunn's Revenge
  - Titan's Bane
  starter: *id001
  aspect: Aspect of the Heroic Tutor
- source: suggested
  archetype: cooldown
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Arondight
  - Heartseeker
  - Avatar's Parashu
  - Titan's Bane
  flex_slots:
  - Hydra's Lament
  - Arondight
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    Tyrfing, Damaru, Genji''s Guard, Pendulum Blade, Tekko-Kagi, Silverbranch Bow,
    Rage, Breastplate of Valor, Riptalon, Chandra''s Grace, Lernaean Bow, Dominance,
    Deathbringer, Toxic Blade, Golden Blade, Runeforged Hammer, Bloodforge, Barbed
    Carver, Qin''s Blade, Screeching Gargoyle, Demon Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.65
      win: 0.56
      pick: 0.86
      fit: 0.57
    Hydra's Lament:
      total: 0.52
      efficiency: 0.55
      win: 0.56
      pick: 0.0
      fit: 0.52
    Arondight:
      total: 0.5
      efficiency: 0.53
      win: 0.56
      pick: 0.0
      fit: 0.42
    Heartseeker:
      total: 0.53
      efficiency: 0.45
      win: 0.61
      pick: 0.63
      fit: 0.45
    Avatar's Parashu:
      total: 0.54
      efficiency: 0.46
      win: 0.73
      pick: 0.28
      fit: 0.25
    Titan's Bane:
      total: 0.6
      efficiency: 0.48
      win: 0.81
      pick: 0.3
      fit: 0.35
  community_ordered:
  - Jotunn's Revenge
  - Heartseeker
  - Avatar's Parashu
  - Titan's Bane
  starter: *id001
  aspect: Aspect of the Heroic Tutor
- source: suggested
  archetype: model
  slot_order:
  - Transcendence
  - Jotunn's Revenge
  - Tyrfing
  - The Crusher
  - Hydra's Lament
  - The Reaper
  flex_slots:
  - Tyrfing
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: The Reaper, Hydra''s Lament, Tyrfing, Tekko-Kagi, Rage,
    Arondight, Deathbringer, Riptalon, Silverbranch Bow, Lernaean Bow, Dominance,
    Pendulum Blade, Demon Blade, Golden Blade, Bloodforge, Musashi''s Dual Swords,
    Barbed Carver, Toxic Blade, Runeforged Hammer, Damaru, Genji''s Guard, Shield
    Splitter, Eye of the Storm, Avenging Blade.'
  slot_scores:
    Transcendence:
      total: 0.5
      efficiency: 0.5
      win: 0.56
      pick: 0.79
      fit: 0.2
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.65
      win: 0.56
      pick: 0.86
      fit: 0.53
    Tyrfing:
      total: 0.51
      efficiency: 0.53
      win: 0.56
      pick: 0.0
      fit: 0.45
    The Crusher:
      total: 0.51
      efficiency: 0.51
      win: 0.5
      pick: 0.53
      fit: 0.51
    Hydra's Lament:
      total: 0.51
      efficiency: 0.55
      win: 0.56
      pick: 0.0
      fit: 0.42
    The Reaper:
      total: 0.53
      efficiency: 0.57
      win: 0.56
      pick: 0.0
      fit: 0.53
  community_ordered:
  - Transcendence
  - Jotunn's Revenge
  - The Crusher
  starter: *id001
  aspect: Aspect of the Heroic Tutor
---
