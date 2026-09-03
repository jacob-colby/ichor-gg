---
type: smite-build
god: Chiron
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Heroic Tutor
  aspect_pick_rate: 0.27
  aspect_win_rate: 0.53
  slot_order:
  - name: Transcendence
    pick_rate: 0.33
    win_rate: 0.49
    alternates:
    - name: Tyrfing
      pick_rate: 0.25
      win_rate: 0.51
    - name: Daybreak Gavel
      pick_rate: 0.12
      win_rate: 0.55
  - name: Jotunn's Revenge
    pick_rate: 0.29
    win_rate: 0.49
    alternates:
    - name: Odysseus' Bow
      pick_rate: 0.13
      win_rate: 0.55
    - name: Toxic Blade
      pick_rate: 0.07
      win_rate: 0.61
  - name: Odysseus' Bow
    pick_rate: 0.14
    win_rate: 0.52
    alternates:
    - name: Heartseeker
      pick_rate: 0.13
      win_rate: 0.53
    - name: The Crusher
      pick_rate: 0.13
      win_rate: 0.54
  - name: Heartseeker
    pick_rate: 0.13
    win_rate: 0.46
    alternates:
    - name: The Executioner
      pick_rate: 0.12
      win_rate: 0.66
    - name: Titan's Bane
      pick_rate: 0.11
      win_rate: 0.5
  - name: Titan's Bane
    pick_rate: 0.13
    win_rate: 0.55
    alternates:
    - name: Silverbranch Bow
      pick_rate: 0.09
      win_rate: 0.63
    - name: The Crusher
      pick_rate: 0.07
      win_rate: 0.52
  - name: Avatar's Parashu
    pick_rate: 0.09
    win_rate: 0.78
    alternates:
    - name: Hunter's Bow
      pick_rate: 0.08
      win_rate: 0.5
    - name: Skeggox
      pick_rate: 0.06
      win_rate: 0.4
  community_starters:
  - name: Hunter's Cowl
    pick_rate: 0.24
    win_rate: 0.57
  - name: Bluestone Brooch
    pick_rate: 0.22
    win_rate: 0.53
  - name: Bluestone Pendant
    pick_rate: 0.13
    win_rate: 0.4
  source_url: https://smitebrain.com/gods/chiron/
  last_verified: '2026-09-03'
  god_win_rate: 0.5134529147982063
  god_matches_won: 229
  god_matches_played: 446
  god_division: obsidian
  god_window_start: '2026-08-25'
  god_window_end: '2026-09-03'
  god_matches_analyzed: 10626
  starter:
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: core
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - Tyrfing
  - Riptalon
  - Silverbranch Bow
  - Avatar's Parashu
  flex_slots:
  - Riptalon
  - Tyrfing
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Toxic Blade, Riptalon, Tekko-Kagi, Lernaean Bow, The Reaper, Hydra''s
    Lament, Deathbringer, Golden Blade, Dominance, Demon Blade, Musashi''s Dual Swords,
    Arondight, Pendulum Blade, Damaru, Rage, Runeforged Hammer, Qin''s Blade, Berserker''s
    Shield, Avenging Blade, Barbed Carver, Sun Beam Bow, Bloodforge.'
  slot_scores:
    Toxic Blade:
      total: 0.5
      efficiency: 0.44
      win: 0.61
      pick: 0.1
      fit: 0.47
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.49
      pick: 0.4
      fit: 0.44
    Tyrfing:
      total: 0.5
      efficiency: 0.48
      win: 0.51
      pick: 0.25
      fit: 0.57
    Riptalon:
      total: 0.5
      efficiency: 0.51
      win: 0.53
      pick: 0.0
      fit: 0.56
    Silverbranch Bow:
      total: 0.55
      efficiency: 0.53
      win: 0.63
      pick: 0.19
      fit: 0.47
    Avatar's Parashu:
      total: 0.57
      efficiency: 0.45
      win: 0.78
      pick: 0.28
      fit: 0.34
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: mana-stack
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Dominance
  - Silverbranch Bow
  - Titan's Bane
  - Avatar's Parashu
  flex_slots:
  - Titan's Bane
  - Dominance
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Hydra''s
    Lament, Lernaean Bow, The Reaper, Toxic Blade, Tekko-Kagi, Riptalon, Dominance,
    Deathbringer, Golden Blade, Arondight, Musashi''s Dual Swords, Demon Blade, Runeforged
    Hammer, Pendulum Blade, Damaru, Rage, Avenging Blade, Qin''s Blade, Barbed Carver,
    Berserker''s Shield, Breastplate of Valor, Genji''s Guard.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.49
      pick: 0.4
      fit: 0.44
    Hydra's Lament:
      total: 0.49
      efficiency: 0.54
      win: 0.53
      pick: 0.0
      fit: 0.42
    Dominance:
      total: 0.47
      efficiency: 0.45
      win: 0.53
      pick: 0.0
      fit: 0.5
    Silverbranch Bow:
      total: 0.52
      efficiency: 0.53
      win: 0.63
      pick: 0.19
      fit: 0.32
    Titan's Bane:
      total: 0.48
      efficiency: 0.47
      win: 0.55
      pick: 0.28
      fit: 0.39
    Avatar's Parashu:
      total: 0.57
      efficiency: 0.45
      win: 0.78
      pick: 0.28
      fit: 0.29
  starter: *id001
- source: suggested
  archetype: crit
  slot_order:
  - Jotunn's Revenge
  - Musashi's Dual Swords
  - Silverbranch Bow
  - Demon Blade
  - Deathbringer
  - Avatar's Parashu
  flex_slots:
  - Demon Blade
  - Musashi's Dual Swords
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
    this god: Toxic Blade, Riptalon, The Reaper, Tekko-Kagi, Lernaean Bow, Hydra''s
    Lament, Deathbringer, Demon Blade, Golden Blade, Dominance, Musashi''s Dual Swords,
    Arondight, Damaru, Rage, Pendulum Blade, Qin''s Blade, Runeforged Hammer, Berserker''s
    Shield, Avenging Blade, Barbed Carver, Sun Beam Bow, Bloodforge.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.49
      pick: 0.4
      fit: 0.41
    Musashi's Dual Swords:
      total: 0.46
      efficiency: 0.46
      win: 0.53
      pick: 0.0
      fit: 0.42
    Silverbranch Bow:
      total: 0.55
      efficiency: 0.53
      win: 0.63
      pick: 0.19
      fit: 0.46
    Demon Blade:
      total: 0.47
      efficiency: 0.38
      win: 0.53
      pick: 0.0
      fit: 0.64
    Deathbringer:
      total: 0.48
      efficiency: 0.51
      win: 0.53
      pick: 0.0
      fit: 0.42
    Avatar's Parashu:
      total: 0.57
      efficiency: 0.45
      win: 0.78
      pick: 0.28
      fit: 0.32
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - The Reaper
  - Silverbranch Bow
  - Titan's Bane
  - Avatar's Parashu
  flex_slots:
  - Titan's Bane
  - The Reaper
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Toxic Blade, The Reaper, Riptalon, Tekko-Kagi, Hydra''s Lament, Lernaean
    Bow, Deathbringer, Pendulum Blade, Dominance, Golden Blade, Arondight, Musashi''s
    Dual Swords, Demon Blade, Runeforged Hammer, Daybreak Gavel, Damaru, Rage, Qin''s
    Blade, Avenging Blade, Berserker''s Shield, Breastplate of Valor, Barbed Carver.'
  slot_scores:
    Toxic Blade:
      total: 0.49
      efficiency: 0.44
      win: 0.61
      pick: 0.1
      fit: 0.42
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.49
      pick: 0.4
      fit: 0.46
    The Reaper:
      total: 0.49
      efficiency: 0.55
      win: 0.53
      pick: 0.0
      fit: 0.39
    Silverbranch Bow:
      total: 0.54
      efficiency: 0.53
      win: 0.63
      pick: 0.19
      fit: 0.42
    Titan's Bane:
      total: 0.49
      efficiency: 0.47
      win: 0.55
      pick: 0.28
      fit: 0.43
    Avatar's Parashu:
      total: 0.57
      efficiency: 0.45
      win: 0.78
      pick: 0.28
      fit: 0.33
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Riptalon
  - Silverbranch Bow
  - Avatar's Parashu
  - Amanita Charm
  flex_slots:
  - Silverbranch Bow
  - Riptalon
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
    the Phoenix, Toxic Blade, Kinetic Cuirass, Genji''s Guard, Freya''s Tears, Breastplate
    of Valor, Runeforged Hammer, Golden Blade, Yogi''s Necklace, Shifter''s Shield,
    Daybreak Gavel, Shield Splitter, Lernaean Bow, Pharaoh''s Curse, Hydra''s Lament,
    Chandra''s Grace, Shogun''s Ofuda, Phoenix Feather, Eye of the Storm, Tekko-Kagi,
    Erosion, Eye of Providence.'
  slot_scores:
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.53
      pick: 0.0
      fit: 0.38
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.49
      pick: 0.4
      fit: 0.3
    Riptalon:
      total: 0.52
      efficiency: 0.51
      win: 0.53
      pick: 0.0
      fit: 0.68
    Silverbranch Bow:
      total: 0.53
      efficiency: 0.53
      win: 0.63
      pick: 0.19
      fit: 0.32
    Avatar's Parashu:
      total: 0.56
      efficiency: 0.45
      win: 0.78
      pick: 0.28
      fit: 0.23
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.62
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - The Executioner
  - Toxic Blade
  - Jotunn's Revenge
  - Riptalon
  - Silverbranch Bow
  - Avatar's Parashu
  flex_slots:
  - Toxic Blade
  - Riptalon
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Toxic Blade, Riptalon, The Reaper, Tekko-Kagi, Lernaean Bow, Hydra''s
    Lament, Avenging Blade, Deathbringer, Pendulum Blade, Golden Blade, Dominance,
    Demon Blade, Musashi''s Dual Swords, Arondight, Oath-Sworn Spear, Runeforged Hammer,
    Damaru, Rage, Qin''s Blade, Berserker''s Shield, Screeching Gargoyle.'
  slot_scores:
    The Executioner:
      total: 0.52
      efficiency: 0.35
      win: 0.66
      pick: 0.2
      fit: 0.6
    Toxic Blade:
      total: 0.52
      efficiency: 0.44
      win: 0.61
      pick: 0.1
      fit: 0.56
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.49
      pick: 0.4
      fit: 0.53
    Riptalon:
      total: 0.51
      efficiency: 0.51
      win: 0.53
      pick: 0.0
      fit: 0.63
    Silverbranch Bow:
      total: 0.56
      efficiency: 0.53
      win: 0.63
      pick: 0.19
      fit: 0.56
    Avatar's Parashu:
      total: 0.59
      efficiency: 0.45
      win: 0.78
      pick: 0.28
      fit: 0.45
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - Tyrfing
  - Riptalon
  - Silverbranch Bow
  - Avatar's Parashu
  flex_slots:
  - Riptalon
  - Tyrfing
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Toxic Blade, Riptalon, Lernaean Bow, Tekko-Kagi, The Reaper, Golden
    Blade, Hydra''s Lament, Deathbringer, Dominance, Qin''s Blade, Demon Blade, Musashi''s
    Dual Swords, Arondight, Sun Beam Bow, Pendulum Blade, Runeforged Hammer, Berserker''s
    Shield, Damaru, Rage, Avenging Blade, Dagger of Frenzy, Barbed Carver.'
  slot_scores:
    Toxic Blade:
      total: 0.51
      efficiency: 0.44
      win: 0.61
      pick: 0.1
      fit: 0.52
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.49
      pick: 0.4
      fit: 0.35
    Tyrfing:
      total: 0.5
      efficiency: 0.48
      win: 0.51
      pick: 0.25
      fit: 0.6
    Riptalon:
      total: 0.51
      efficiency: 0.51
      win: 0.53
      pick: 0.0
      fit: 0.6
    Silverbranch Bow:
      total: 0.56
      efficiency: 0.53
      win: 0.63
      pick: 0.19
      fit: 0.52
    Avatar's Parashu:
      total: 0.56
      efficiency: 0.45
      win: 0.78
      pick: 0.28
      fit: 0.26
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - Hydra's Lament
  - Arondight
  - Silverbranch Bow
  - Avatar's Parashu
  flex_slots:
  - Toxic Blade
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Hydra''s Lament, Toxic Blade, Riptalon,
    Lernaean Bow, The Reaper, Tekko-Kagi, Arondight, Pendulum Blade, Deathbringer,
    Dominance, Golden Blade, Breastplate of Valor, Musashi''s Dual Swords, Genji''s
    Guard, Demon Blade, Daybreak Gavel, Qin''s Blade, Runeforged Hammer, Berserker''s
    Shield, Damaru, Rage, Avenging Blade.'
  slot_scores:
    Toxic Blade:
      total: 0.49
      efficiency: 0.44
      win: 0.61
      pick: 0.1
      fit: 0.36
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.49
      pick: 0.4
      fit: 0.49
    Hydra's Lament:
      total: 0.5
      efficiency: 0.54
      win: 0.53
      pick: 0.0
      fit: 0.46
    Arondight:
      total: 0.47
      efficiency: 0.5
      win: 0.53
      pick: 0.0
      fit: 0.36
    Silverbranch Bow:
      total: 0.53
      efficiency: 0.53
      win: 0.63
      pick: 0.19
      fit: 0.36
    Avatar's Parashu:
      total: 0.55
      efficiency: 0.45
      win: 0.78
      pick: 0.28
      fit: 0.21
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
    Underrated for this god: Riptalon, Tekko-Kagi, Lernaean Bow, The Reaper, Hydra''s
    Lament, Deathbringer, Golden Blade, Dominance, Demon Blade, Toxic Blade, Musashi''s
    Dual Swords, Arondight, Pendulum Blade, Damaru, Rage, Runeforged Hammer, Qin''s
    Blade, Berserker''s Shield, Avenging Blade, Barbed Carver, Sun Beam Bow, Bloodforge.'
  slot_scores:
    Lernaean Bow:
      total: 0.49
      efficiency: 0.52
      win: 0.53
      pick: 0.0
      fit: 0.5
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.49
      pick: 0.4
      fit: 0.44
    The Reaper:
      total: 0.49
      efficiency: 0.55
      win: 0.53
      pick: 0.0
      fit: 0.43
    Riptalon:
      total: 0.5
      efficiency: 0.51
      win: 0.53
      pick: 0.0
      fit: 0.56
    Silverbranch Bow:
      total: 0.55
      efficiency: 0.53
      win: 0.63
      pick: 0.19
      fit: 0.47
    Tekko-Kagi:
      total: 0.5
      efficiency: 0.49
      win: 0.53
      pick: 0.0
      fit: 0.58
  starter: *id001
- source: suggested
  archetype: hybrid
  slot_order:
  - Lernaean Bow
  - Jotunn's Revenge
  - The Reaper
  - Riptalon
  - Tekko-Kagi
  - Avatar's Parashu
  flex_slots:
  - The Reaper
  - Avatar's Parashu
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s core, corrected where the community is clearly right (efficiency
    + fit + win/pick). Underrated for this god: Riptalon, Tekko-Kagi, Lernaean Bow,
    The Reaper, Hydra''s Lament, Deathbringer, Golden Blade, Dominance, Demon Blade,
    Toxic Blade, Musashi''s Dual Swords, Arondight, Pendulum Blade, Damaru, Rage,
    Runeforged Hammer, Qin''s Blade, Berserker''s Shield, Avenging Blade, Barbed Carver,
    Sun Beam Bow, Bloodforge.'
  slot_scores:
    Lernaean Bow:
      total: 0.49
      efficiency: 0.52
      win: 0.53
      pick: 0.0
      fit: 0.5
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.49
      pick: 0.4
      fit: 0.44
    The Reaper:
      total: 0.49
      efficiency: 0.55
      win: 0.53
      pick: 0.0
      fit: 0.43
    Riptalon:
      total: 0.5
      efficiency: 0.51
      win: 0.53
      pick: 0.0
      fit: 0.56
    Tekko-Kagi:
      total: 0.5
      efficiency: 0.49
      win: 0.53
      pick: 0.0
      fit: 0.58
    Avatar's Parashu:
      total: 0.57
      efficiency: 0.45
      win: 0.78
      pick: 0.28
      fit: 0.34
  swaps:
  - added: Avatar's Parashu
    removed: Silverbranch Bow
    reason: community 78% win over 40 matches (vs 51% on this god), taking the model's
      weakest slot from Silverbranch Bow
  starter: *id001
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - The Reaper
  - Silverbranch Bow
  - The Crusher
  - Titan's Bane
  - Avatar's Parashu
  flex_slots:
  - Titan's Bane
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    this god: The Reaper, Hydra''s Lament, Deathbringer, Riptalon, Toxic Blade, Tekko-Kagi,
    Lernaean Bow, Musashi''s Dual Swords, Pendulum Blade, Arondight, Damaru, Rage,
    Demon Blade, Golden Blade, Dominance, Runeforged Hammer, Barbed Carver, Avenging
    Blade, Bloodforge, Qin''s Blade, Shield Splitter, Breastplate of Valor.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.49
      pick: 0.4
      fit: 0.53
    The Reaper:
      total: 0.51
      efficiency: 0.55
      win: 0.53
      pick: 0.0
      fit: 0.53
    Silverbranch Bow:
      total: 0.53
      efficiency: 0.53
      win: 0.63
      pick: 0.19
      fit: 0.36
    The Crusher:
      total: 0.49
      efficiency: 0.47
      win: 0.54
      pick: 0.2
      fit: 0.51
    Titan's Bane:
      total: 0.5
      efficiency: 0.47
      win: 0.55
      pick: 0.28
      fit: 0.51
    Avatar's Parashu:
      total: 0.59
      efficiency: 0.45
      win: 0.78
      pick: 0.28
      fit: 0.41
  starter: *id001
  aspect: Aspect of the Heroic Tutor
- source: suggested
  archetype: mana-stack
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - Silverbranch Bow
  - Heartseeker
  - Avatar's Parashu
  flex_slots:
  - Heartseeker
  - Transcendence
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Hydra''s
    Lament, The Reaper, Deathbringer, Lernaean Bow, Tekko-Kagi, Toxic Blade, Riptalon,
    Arondight, Musashi''s Dual Swords, Dominance, Pendulum Blade, Runeforged Hammer,
    Golden Blade, Damaru, Rage, Avenging Blade, Demon Blade, Barbed Carver, Breastplate
    of Valor, Bloodforge, Genji''s Guard, Shield Splitter.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.49
      pick: 0.4
      fit: 0.5
    Transcendence:
      total: 0.46
      efficiency: 0.53
      win: 0.49
      pick: 0.33
      fit: 0.27
    Hydra's Lament:
      total: 0.5
      efficiency: 0.54
      win: 0.53
      pick: 0.0
      fit: 0.47
    Silverbranch Bow:
      total: 0.51
      efficiency: 0.53
      win: 0.63
      pick: 0.19
      fit: 0.22
    Heartseeker:
      total: 0.47
      efficiency: 0.47
      win: 0.46
      pick: 0.22
      fit: 0.6
    Avatar's Parashu:
      total: 0.57
      efficiency: 0.45
      win: 0.78
      pick: 0.28
      fit: 0.33
  starter: *id001
  aspect: Aspect of the Heroic Tutor
- source: suggested
  archetype: crit
  slot_order:
  - Jotunn's Revenge
  - Musashi's Dual Swords
  - Silverbranch Bow
  - Demon Blade
  - Deathbringer
  - Avatar's Parashu
  flex_slots:
  - Demon Blade
  - Musashi's Dual Swords
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
    this god: Toxic Blade, Riptalon, The Reaper, Tekko-Kagi, Lernaean Bow, Hydra''s
    Lament, Deathbringer, Demon Blade, Golden Blade, Dominance, Musashi''s Dual Swords,
    Arondight, Damaru, Rage, Pendulum Blade, Qin''s Blade, Runeforged Hammer, Berserker''s
    Shield, Avenging Blade, Barbed Carver, Sun Beam Bow, Bloodforge.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.49
      pick: 0.4
      fit: 0.41
    Musashi's Dual Swords:
      total: 0.46
      efficiency: 0.46
      win: 0.53
      pick: 0.0
      fit: 0.42
    Silverbranch Bow:
      total: 0.55
      efficiency: 0.53
      win: 0.63
      pick: 0.19
      fit: 0.46
    Demon Blade:
      total: 0.47
      efficiency: 0.38
      win: 0.53
      pick: 0.0
      fit: 0.64
    Deathbringer:
      total: 0.48
      efficiency: 0.51
      win: 0.53
      pick: 0.0
      fit: 0.42
    Avatar's Parashu:
      total: 0.57
      efficiency: 0.45
      win: 0.78
      pick: 0.28
      fit: 0.32
  starter: *id001
  aspect: Aspect of the Heroic Tutor
- source: suggested
  archetype: burst
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - The Reaper
  - Silverbranch Bow
  - Titan's Bane
  - Avatar's Parashu
  flex_slots:
  - The Reaper
  - Hydra's Lament
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
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: The Reaper, Hydra''s Lament, Toxic Blade, Riptalon, Tekko-Kagi, Deathbringer,
    Pendulum Blade, Lernaean Bow, Arondight, Musashi''s Dual Swords, Runeforged Hammer,
    Golden Blade, Dominance, Damaru, Rage, Daybreak Gavel, Demon Blade, Avenging Blade,
    Barbed Carver, Breastplate of Valor, Genji''s Guard, Bloodforge.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.49
      pick: 0.4
      fit: 0.53
    Hydra's Lament:
      total: 0.49
      efficiency: 0.54
      win: 0.53
      pick: 0.0
      fit: 0.4
    The Reaper:
      total: 0.5
      efficiency: 0.55
      win: 0.53
      pick: 0.0
      fit: 0.45
    Silverbranch Bow:
      total: 0.53
      efficiency: 0.53
      win: 0.63
      pick: 0.19
      fit: 0.33
    Titan's Bane:
      total: 0.5
      efficiency: 0.47
      win: 0.55
      pick: 0.28
      fit: 0.48
    Avatar's Parashu:
      total: 0.58
      efficiency: 0.45
      win: 0.78
      pick: 0.28
      fit: 0.38
  starter: *id001
  aspect: Aspect of the Heroic Tutor
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - The Reaper
  - Silverbranch Bow
  - Avatar's Parashu
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Silverbranch Bow
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
    Daybreak Gavel, Pharaoh''s Curse, Eye of the Storm, Umbral Link, Golden Blade,
    Phoenix Feather, Chandra''s Grace, Hydra''s Lament, Shogun''s Ofuda, Eye of Providence,
    Void Shield, Stampede, Draconic Scale, Avenging Blade.'
  slot_scores:
    Berserker's Shield:
      total: 0.52
      efficiency: 0.68
      win: 0.53
      pick: 0.0
      fit: 0.3
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.49
      pick: 0.4
      fit: 0.34
    The Reaper:
      total: 0.53
      efficiency: 0.55
      win: 0.53
      pick: 0.0
      fit: 0.63
    Silverbranch Bow:
      total: 0.51
      efficiency: 0.53
      win: 0.63
      pick: 0.19
      fit: 0.23
    Avatar's Parashu:
      total: 0.56
      efficiency: 0.45
      win: 0.78
      pick: 0.28
      fit: 0.26
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.77
  starter: *id001
  aspect: Aspect of the Heroic Tutor
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - The Reaper
  - Silverbranch Bow
  - The Crusher
  - Titan's Bane
  - Avatar's Parashu
  flex_slots:
  - Titan's Bane
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    for this god: The Reaper, Toxic Blade, Riptalon, Tekko-Kagi, Hydra''s Lament,
    Pendulum Blade, Avenging Blade, Deathbringer, Lernaean Bow, Musashi''s Dual Swords,
    Arondight, Oath-Sworn Spear, Damaru, Rage, Golden Blade, Runeforged Hammer, Dominance,
    Demon Blade, Barbed Carver, Screeching Gargoyle, Bloodforge.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.49
      pick: 0.4
      fit: 0.62
    The Reaper:
      total: 0.52
      efficiency: 0.55
      win: 0.53
      pick: 0.0
      fit: 0.62
    Silverbranch Bow:
      total: 0.55
      efficiency: 0.53
      win: 0.63
      pick: 0.19
      fit: 0.48
    The Crusher:
      total: 0.51
      efficiency: 0.47
      win: 0.54
      pick: 0.2
      fit: 0.63
    Titan's Bane:
      total: 0.52
      efficiency: 0.47
      win: 0.55
      pick: 0.28
      fit: 0.63
    Avatar's Parashu:
      total: 0.6
      efficiency: 0.45
      win: 0.78
      pick: 0.28
      fit: 0.53
  starter: *id001
  aspect: Aspect of the Heroic Tutor
- source: suggested
  archetype: attack-speed
  slot_order:
  - Toxic Blade
  - Jotunn's Revenge
  - Tyrfing
  - Riptalon
  - Silverbranch Bow
  - Avatar's Parashu
  flex_slots:
  - Riptalon
  - Tyrfing
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Toxic Blade, Riptalon, Lernaean Bow, Tekko-Kagi, The Reaper, Golden
    Blade, Hydra''s Lament, Deathbringer, Dominance, Qin''s Blade, Demon Blade, Musashi''s
    Dual Swords, Arondight, Sun Beam Bow, Pendulum Blade, Runeforged Hammer, Berserker''s
    Shield, Damaru, Rage, Avenging Blade, Dagger of Frenzy, Barbed Carver.'
  slot_scores:
    Toxic Blade:
      total: 0.51
      efficiency: 0.44
      win: 0.61
      pick: 0.1
      fit: 0.52
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.49
      pick: 0.4
      fit: 0.35
    Tyrfing:
      total: 0.5
      efficiency: 0.48
      win: 0.51
      pick: 0.25
      fit: 0.6
    Riptalon:
      total: 0.51
      efficiency: 0.51
      win: 0.53
      pick: 0.0
      fit: 0.6
    Silverbranch Bow:
      total: 0.56
      efficiency: 0.53
      win: 0.63
      pick: 0.19
      fit: 0.52
    Avatar's Parashu:
      total: 0.56
      efficiency: 0.45
      win: 0.78
      pick: 0.28
      fit: 0.26
  starter: *id001
  aspect: Aspect of the Heroic Tutor
- source: suggested
  archetype: cooldown
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - The Reaper
  - Arondight
  - Silverbranch Bow
  - Avatar's Parashu
  flex_slots:
  - The Reaper
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
    Pendulum Blade, Toxic Blade, Riptalon, Deathbringer, Lernaean Bow, Tekko-Kagi,
    Breastplate of Valor, Musashi''s Dual Swords, Genji''s Guard, Runeforged Hammer,
    Daybreak Gavel, Golden Blade, Damaru, Rage, Dominance, Demon Blade, Avenging Blade,
    Eye of Erebus, Barbed Carver.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.49
      pick: 0.4
      fit: 0.57
    Hydra's Lament:
      total: 0.51
      efficiency: 0.54
      win: 0.53
      pick: 0.0
      fit: 0.52
    The Reaper:
      total: 0.48
      efficiency: 0.55
      win: 0.53
      pick: 0.0
      fit: 0.33
    Arondight:
      total: 0.48
      efficiency: 0.5
      win: 0.53
      pick: 0.0
      fit: 0.42
    Silverbranch Bow:
      total: 0.52
      efficiency: 0.53
      win: 0.63
      pick: 0.19
      fit: 0.26
    Avatar's Parashu:
      total: 0.56
      efficiency: 0.45
      win: 0.78
      pick: 0.28
      fit: 0.25
  starter: *id001
  aspect: Aspect of the Heroic Tutor
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - The Reaper
  - Deathbringer
  - Heartseeker
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
    Tekko-Kagi, Lernaean Bow, Musashi''s Dual Swords, Pendulum Blade, Arondight, Damaru,
    Rage, Demon Blade, Golden Blade, Dominance, Runeforged Hammer, Toxic Blade, Barbed
    Carver, Avenging Blade, Bloodforge, Qin''s Blade, Shield Splitter, Breastplate
    of Valor.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.49
      pick: 0.4
      fit: 0.53
    Transcendence:
      total: 0.45
      efficiency: 0.53
      win: 0.49
      pick: 0.33
      fit: 0.2
    Hydra's Lament:
      total: 0.49
      efficiency: 0.54
      win: 0.53
      pick: 0.0
      fit: 0.42
    The Reaper:
      total: 0.51
      efficiency: 0.55
      win: 0.53
      pick: 0.0
      fit: 0.53
    Deathbringer:
      total: 0.49
      efficiency: 0.51
      win: 0.53
      pick: 0.0
      fit: 0.49
    Heartseeker:
      total: 0.47
      efficiency: 0.47
      win: 0.46
      pick: 0.22
      fit: 0.61
  starter: *id001
  aspect: Aspect of the Heroic Tutor
- source: suggested
  archetype: hybrid
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - The Reaper
  - Deathbringer
  - Heartseeker
  - Avatar's Parashu
  flex_slots:
  - Deathbringer
  - Avatar's Parashu
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s core, corrected where the community is clearly right (efficiency
    + fit + win/pick). Underrated for this god: The Reaper, Hydra''s Lament, Deathbringer,
    Riptalon, Tekko-Kagi, Lernaean Bow, Musashi''s Dual Swords, Pendulum Blade, Arondight,
    Damaru, Rage, Demon Blade, Golden Blade, Dominance, Runeforged Hammer, Toxic Blade,
    Barbed Carver, Avenging Blade, Bloodforge, Qin''s Blade, Shield Splitter, Breastplate
    of Valor.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.49
      pick: 0.4
      fit: 0.53
    Hydra's Lament:
      total: 0.49
      efficiency: 0.54
      win: 0.53
      pick: 0.0
      fit: 0.42
    The Reaper:
      total: 0.51
      efficiency: 0.55
      win: 0.53
      pick: 0.0
      fit: 0.53
    Deathbringer:
      total: 0.49
      efficiency: 0.51
      win: 0.53
      pick: 0.0
      fit: 0.49
    Heartseeker:
      total: 0.47
      efficiency: 0.47
      win: 0.46
      pick: 0.22
      fit: 0.61
    Avatar's Parashu:
      total: 0.59
      efficiency: 0.45
      win: 0.78
      pick: 0.28
      fit: 0.41
  swaps:
  - added: Avatar's Parashu
    removed: Transcendence
    reason: community 78% win over 40 matches (vs 51% on this god), taking the model's
      weakest slot from Transcendence
  starter: *id001
  aspect: Aspect of the Heroic Tutor
---
