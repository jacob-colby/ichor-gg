---
type: smite-build
god: Ares
mode: Conquest
builds:
- source: community
  aspect: Aspect of Reverberation
  aspect_pick_rate: 0.13
  aspect_win_rate: 0.41
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.17
    win_rate: 0.53
    alternates:
    - name: Gauntlet of Thebes
      pick_rate: 0.16
      win_rate: 0.47
    - name: Stampede
      pick_rate: 0.14
      win_rate: 0.57
  - name: Genji's Guard
    pick_rate: 0.19
    win_rate: 0.56
    alternates:
    - name: Stampede
      pick_rate: 0.13
      win_rate: 0.49
    - name: Breastplate of Valor
      pick_rate: 0.1
      win_rate: 0.63
  - name: Breastplate of Valor
    pick_rate: 0.1
    win_rate: 0.53
    alternates:
    - name: Genji's Guard
      pick_rate: 0.18
      win_rate: 0.52
    - name: Stampede
      pick_rate: 0.1
      win_rate: 0.49
  - name: Shell of Rebuke
    pick_rate: 0.1
    win_rate: 0.51
    alternates:
    - name: Genji's Guard
      pick_rate: 0.08
      win_rate: 0.46
    - name: Freya's Tears
      pick_rate: 0.07
      win_rate: 0.7
  - name: Dwarven Plate
    pick_rate: 0.07
    win_rate: 0.57
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.68
    - name: Hide of the Nemean Lion
      pick_rate: 0.06
      win_rate: 0.46
  - name: Medal of Defense
    pick_rate: 0.08
    win_rate: 0.37
    alternates:
    - name: Sage's Ring
      pick_rate: 0.05
      win_rate: 0.54
    - name: Medallion
      pick_rate: 0.05
      win_rate: 0.5
  community_starters:
  - name: Selflessness
    pick_rate: 0.23
    win_rate: 0.52
  - name: War Flag
    pick_rate: 0.15
    win_rate: 0.47
  - name: Warrior's Axe
    pick_rate: 0.15
    win_rate: 0.49
  source_url: https://smitebrain.com/gods/ares/
  last_verified: '2026-08-11'
  god_win_rate: 0.5219047619047619
  god_matches_won: 274
  god_matches_played: 525
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-11'
  god_matches_analyzed: 18835
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Eye of Providence
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Eye of Providence
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Freya''s Tears, Amanita Charm, Kinetic Cuirass, Eye of Providence, Berserker''s
    Shield, Breastplate of Valor, Oni Hunter''s Garb, Gluttonous Grimoire, Shield
    of the Phoenix, Stampede, Erosion, Draconic Scale, Spectral Armor, Jotunn''s Revenge,
    Shield Splitter, Pharaoh''s Curse, Runeforged Hammer, Soul Gem, The Crusher, Leviathan''s
    Hide, Hydra''s Lament, Eye of the Storm, Yogi''s Necklace, Mantle Of Discord,
    Midgardian Mail, Stone of Binding, Shogun''s Ofuda, Helm of Radiance, Magi''s
    Cloak, Gladiator''s Shield, Rod of Asclepius, Ancile, Screeching Gargoyle, Prophetic
    Cloak, Doublet of Binding, Void Shield, Xibalban Effigy, Hide of the Nemean Lion.'
  slot_scores:
    Eye of Providence:
      total: 0.54
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.67
    Genji's Guard:
      total: 0.57
      efficiency: 0.72
      win: 0.56
      pick: 0.19
      fit: 0.38
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.77
    Freya's Tears:
      total: 0.62
      efficiency: 0.59
      win: 0.7
      pick: 0.07
      fit: 0.62
    Shifter's Shield:
      total: 0.54
      efficiency: 0.55
      win: 0.53
      pick: 0.17
      fit: 0.67
    Amanita Charm:
      total: 0.56
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.67
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Freya''s Tears, Amanita Charm, Shield of the Phoenix, Kinetic Cuirass,
    Berserker''s Shield, Eye of Providence, Soul Gem, Gluttonous Grimoire, Breastplate
    of Valor, Rod of Asclepius, Oni Hunter''s Garb, Chandra''s Grace, Stampede, Erosion,
    Phoenix Feather, Spectral Armor, Draconic Scale, Runeforged Hammer, Jotunn''s
    Revenge, Pharaoh''s Curse, Lifebinder, Yogi''s Necklace, Leviathan''s Hide, Eye
    of the Storm, The Crusher, Hydra''s Lament, Blood-Bound Book, Midgardian Mail,
    Shield Splitter, Bancroft''s Talon, Glorious Pridwen, Shogun''s Ofuda, The Reaper,
    Gladiator''s Shield, Ancile, Riptalon, Jade Scepter, Hide of the Nemean Lion.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.72
      win: 0.56
      pick: 0.19
      fit: 0.35
    Berserker's Shield:
      total: 0.54
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.75
    Shield of the Phoenix:
      total: 0.56
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.9
    Freya's Tears:
      total: 0.61
      efficiency: 0.59
      win: 0.7
      pick: 0.07
      fit: 0.55
    Amanita Charm:
      total: 0.6
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.95
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Gluttonous Grimoire
  - The Crusher
  flex_slots:
  - The Crusher
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Freya''s Tears, Gluttonous Grimoire, Amanita Charm, Jotunn''s Revenge,
    The Crusher, Kinetic Cuirass, Soul Gem, Berserker''s Shield, Breastplate of Valor,
    Eye of Providence, Stone of Binding, Oni Hunter''s Garb, Screeching Gargoyle,
    Spear of the Magus, Void Shield, Avenging Blade, Shield of the Phoenix, The Cosmic
    Horror, Void Stone, Spear of Desolation, Erosion, Spectral Armor, Runeforged Hammer,
    Hydra''s Lament, Draconic Scale, Pharaoh''s Curse, Yogi''s Necklace, Obsidian
    Shard, Riptalon, Shield Splitter, The Reaper, Leviathan''s Hide, Silverbranch
    Bow, Helm of Radiance, Midgardian Mail, Eye of the Storm, Rod of Asclepius, Heartseeker.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.72
      win: 0.56
      pick: 0.19
      fit: 0.27
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.57
    Freya's Tears:
      total: 0.59
      efficiency: 0.59
      win: 0.7
      pick: 0.07
      fit: 0.44
    Gluttonous Grimoire:
      total: 0.55
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.62
    The Crusher:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.48
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Freya's Tears
  - Amanita Charm
  - Pharaoh's Curse
  flex_slots:
  - Golden Blade
  - Pharaoh's Curse
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Freya''s Tears, Berserker''s Shield, Amanita Charm, Gluttonous Grimoire,
    Kinetic Cuirass, Breastplate of Valor, Golden Blade, Eye of Providence, Pharaoh''s
    Curse, Oni Hunter''s Garb, The Crusher, Jotunn''s Revenge, Riptalon, Runeforged
    Hammer, Hydra''s Lament, Lernaean Bow, Soul Gem, Shogun''s Ofuda, Shield of the
    Phoenix, Tyrfing, Spectral Armor, Silverbranch Bow, Yogi''s Necklace, Shield Splitter,
    Erosion, Eye of the Storm, Bracer of The Abyss, Draconic Scale, Dominance, Death
    Metal, Leviathan''s Hide, Rod of Asclepius, Helm of Radiance, Avenging Blade,
    Midgardian Mail, Bragi''s Harp, Damaru, Eros'' Bow.'
  slot_scores:
    Golden Blade:
      total: 0.5
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.53
    Genji's Guard:
      total: 0.54
      efficiency: 0.72
      win: 0.56
      pick: 0.19
      fit: 0.21
    Berserker's Shield:
      total: 0.54
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.43
    Freya's Tears:
      total: 0.57
      efficiency: 0.59
      win: 0.7
      pick: 0.07
      fit: 0.34
    Amanita Charm:
      total: 0.51
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.36
    Pharaoh's Curse:
      total: 0.49
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Freya''s Tears, Breastplate of Valor,
    Amanita Charm, Jotunn''s Revenge, Kinetic Cuirass, Shield of the Phoenix, Berserker''s
    Shield, Hydra''s Lament, Soul Gem, Gluttonous Grimoire, Eye of Providence, Oni
    Hunter''s Garb, The Crusher, Chronos'' Pendant, Runeforged Hammer, Screeching
    Gargoyle, Chandra''s Grace, Spear of Desolation, Gladiator''s Shield, Spectral
    Armor, Erosion, Shield Splitter, Yogi''s Necklace, Pharaoh''s Curse, Prophetic
    Cloak, Draconic Scale, Helm of Radiance, Rod of Asclepius, Gem of Focus, Eye of
    the Storm, Arondight, Death Metal, Leviathan''s Hide, Jade Scepter, Midgardian
    Mail, Spear of the Magus, Mantle Of Discord, Hide of the Nemean Lion.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.72
      win: 0.56
      pick: 0.19
      fit: 0.48
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.65
      win: 0.53
      pick: 0.1
      fit: 0.48
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.46
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.62
      efficiency: 0.59
      win: 0.7
      pick: 0.07
      fit: 0.64
    Amanita Charm:
      total: 0.52
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.45
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Eye of Providence
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Kinetic Cuirass, Eye of Providence, Berserker''s
    Shield, Freya''s Tears, Oni Hunter''s Garb, Gluttonous Grimoire, Breastplate of
    Valor, Shield of the Phoenix, Erosion, Draconic Scale, Spectral Armor, Jotunn''s
    Revenge, Shield Splitter, Pharaoh''s Curse, Runeforged Hammer, Soul Gem, The Crusher,
    Leviathan''s Hide, Hydra''s Lament, Eye of the Storm, Yogi''s Necklace, Mantle
    Of Discord, Midgardian Mail, Stone of Binding, Hide of the Nemean Lion, Shogun''s
    Ofuda, Helm of Radiance, Magi''s Cloak, Stampede, Gladiator''s Shield, Rod of
    Asclepius, Ancile, Screeching Gargoyle, Prophetic Cloak, Doublet of Binding, Void
    Shield, Xibalban Effigy.'
  slot_scores:
    Eye of Providence:
      total: 0.54
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.67
    Genji's Guard:
      total: 0.57
      efficiency: 0.72
      win: 0.56
      pick: 0.19
      fit: 0.38
    Berserker's Shield:
      total: 0.54
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.43
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.77
    Freya's Tears:
      total: 0.62
      efficiency: 0.59
      win: 0.7
      pick: 0.07
      fit: 0.62
    Amanita Charm:
      total: 0.56
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.67
  starter: *id001
---
