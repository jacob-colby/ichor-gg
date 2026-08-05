---
type: smite-build
god: Cabrakan
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Rotund Jotunn
  aspect_pick_rate: 0.05
  aspect_win_rate: 0.53
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.49
    win_rate: 0.61
    alternates:
    - name: Runeforged Hammer
      pick_rate: 0.26
      win_rate: 0.63
    - name: Stampede
      pick_rate: 0.03
      win_rate: 0.71
  - name: Breastplate of Valor
    pick_rate: 0.19
    win_rate: 0.58
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.17
      win_rate: 0.64
    - name: Genji's Guard
      pick_rate: 0.16
      win_rate: 0.67
  - name: Genji's Guard
    pick_rate: 0.27
    win_rate: 0.53
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.13
      win_rate: 0.74
    - name: Dwarven Plate
      pick_rate: 0.06
      win_rate: 0.59
  - name: Dwarven Plate
    pick_rate: 0.15
    win_rate: 0.69
    alternates:
    - name: Genji's Guard
      pick_rate: 0.14
      win_rate: 0.61
    - name: Breastplate of Valor
      pick_rate: 0.06
      win_rate: 0.8
  - name: Shell of Rebuke
    pick_rate: 0.08
    win_rate: 0.56
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.12
      win_rate: 0.58
    - name: Glorious Pridwen
      pick_rate: 0.06
      win_rate: 0.54
  - name: Medal of Defense
    pick_rate: 0.05
    win_rate: 0.71
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.06
      win_rate: 0.75
    - name: Shell of Rebuke
      pick_rate: 0.04
      win_rate: 1.0
  source_url: https://smitebrain.com/gods/cabrakan/
  last_verified: '2026-08-01'
  god_win_rate: 0.5912408759124088
  god_matches_won: 162
  god_matches_played: 274
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-01'
  god_matches_analyzed: 4952
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Runeforged Hammer
  - Shifter's Shield
  - Amanita Charm
  - Stampede
  flex_slots:
  - Breastplate of Valor
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Eye of Providence — physical protection
    swap_item: Eye of Providence
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Stampede, Amanita Charm, Kinetic Cuirass, Eye of Providence, Berserker''s
    Shield, Gluttonous Grimoire, Jotunn''s Revenge, Shield Splitter, Oni Hunter''s
    Garb, Freya''s Tears, The Crusher, Hydra''s Lament, Eye of the Storm, Shield of
    the Phoenix, Erosion, Draconic Scale, Spectral Armor, Pharaoh''s Curse, Avenging
    Blade, Soul Gem, Golden Blade, Leviathan''s Hide, Yogi''s Necklace, Death Metal,
    Midgardian Mail, Stone of Binding, Mantle Of Discord, Hide of the Nemean Lion,
    Helm of Radiance, Lernaean Bow, Rod of Asclepius, Shogun''s Ofuda, Magi''s Cloak,
    Damaru, Ancile, Wyrmskin Hide.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.72
      win: 0.53
      pick: 0.27
      fit: 0.31
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.65
      win: 0.58
      pick: 0.19
      fit: 0.31
    Runeforged Hammer:
      total: 0.58
      efficiency: 0.61
      win: 0.63
      pick: 0.26
      fit: 0.48
    Shifter's Shield:
      total: 0.58
      efficiency: 0.56
      win: 0.61
      pick: 0.49
      fit: 0.57
    Amanita Charm:
      total: 0.54
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.57
    Stampede:
      total: 0.56
      efficiency: 0.53
      win: 0.71
      pick: 0.03
      fit: 0.37
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Shield of the Phoenix
  - Runeforged Hammer
  - Shifter's Shield
  - Amanita Charm
  - Stampede
  flex_slots:
  - Shield of the Phoenix
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Berserker''s
    Shield, Eye of Providence, Soul Gem, Rod of Asclepius, Gluttonous Grimoire, Jotunn''s
    Revenge, Oni Hunter''s Garb, The Crusher, Chandra''s Grace, Hydra''s Lament, Eye
    of the Storm, The Reaper, Shield Splitter, Freya''s Tears, Erosion, Phoenix Feather,
    Spectral Armor, Glorious Pridwen, Avenging Blade, Draconic Scale, Golden Blade,
    Lifebinder, Pharaoh''s Curse, Blood-Bound Book, Yogi''s Necklace, Bancroft''s
    Talon, Leviathan''s Hide, Death Metal, Midgardian Mail, Riptalon, Hide of the
    Nemean Lion, Lernaean Bow, Shogun''s Ofuda.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.72
      win: 0.53
      pick: 0.27
      fit: 0.28
    Shield of the Phoenix:
      total: 0.55
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.8
    Runeforged Hammer:
      total: 0.59
      efficiency: 0.61
      win: 0.63
      pick: 0.26
      fit: 0.54
    Shifter's Shield:
      total: 0.58
      efficiency: 0.56
      win: 0.61
      pick: 0.49
      fit: 0.56
    Amanita Charm:
      total: 0.59
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.86
    Stampede:
      total: 0.56
      efficiency: 0.53
      win: 0.71
      pick: 0.03
      fit: 0.38
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Genji's Guard
  - Runeforged Hammer
  - Gluttonous Grimoire
  - Shifter's Shield
  - The Crusher
  - Stampede
  flex_slots:
  - Genji's Guard
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, The Crusher, Jotunn''s Revenge, Amanita Charm,
    Kinetic Cuirass, Berserker''s Shield, Avenging Blade, Soul Gem, Eye of Providence,
    Stone of Binding, Oni Hunter''s Garb, Screeching Gargoyle, Void Shield, Spear
    of the Magus, Hydra''s Lament, Freya''s Tears, Shield Splitter, Void Stone, The
    Reaper, The Cosmic Horror, Shield of the Phoenix, Eye of the Storm, Spear of Desolation,
    Erosion, Spectral Armor, Heartseeker, Yogi''s Necklace, Pharaoh''s Curse, Draconic
    Scale, Obsidian Shard, Riptalon, Death Metal, Golden Blade, Leviathan''s Hide,
    Silverbranch Bow, Lernaean Bow.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.72
      win: 0.53
      pick: 0.27
      fit: 0.23
    Runeforged Hammer:
      total: 0.57
      efficiency: 0.61
      win: 0.63
      pick: 0.26
      fit: 0.38
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.56
    Shifter's Shield:
      total: 0.56
      efficiency: 0.56
      win: 0.61
      pick: 0.49
      fit: 0.42
    The Crusher:
      total: 0.54
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.56
    Stampede:
      total: 0.55
      efficiency: 0.53
      win: 0.71
      pick: 0.03
      fit: 0.27
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Runeforged Hammer
  - Shifter's Shield
  - Stampede
  - Pharaoh's Curse
  flex_slots:
  - Golden Blade
  - Pharaoh's Curse
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Amanita Charm, Kinetic Cuirass, Gluttonous Grimoire,
    Golden Blade, Eye of Providence, Pharaoh''s Curse, Oni Hunter''s Garb, The Crusher,
    Jotunn''s Revenge, Riptalon, Lernaean Bow, Freya''s Tears, Hydra''s Lament, Soul
    Gem, Shogun''s Ofuda, Tyrfing, Shield of the Phoenix, Shield Splitter, Silverbranch
    Bow, Spectral Armor, Yogi''s Necklace, Erosion, Eye of the Storm, Draconic Scale,
    Bracer of The Abyss, Dominance, Leviathan''s Hide, Death Metal, Rod of Asclepius,
    Helm of Radiance, Avenging Blade, Bragi''s Harp, Midgardian Mail, Eros'' Bow,
    Hide of the Nemean Lion.'
  slot_scores:
    Golden Blade:
      total: 0.5
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.54
    Berserker's Shield:
      total: 0.54
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.43
    Runeforged Hammer:
      total: 0.56
      efficiency: 0.61
      win: 0.63
      pick: 0.26
      fit: 0.31
    Shifter's Shield:
      total: 0.55
      efficiency: 0.56
      win: 0.61
      pick: 0.49
      fit: 0.37
    Stampede:
      total: 0.54
      efficiency: 0.53
      win: 0.71
      pick: 0.03
      fit: 0.24
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
  - Runeforged Hammer
  - Freya's Tears
  - Shifter's Shield
  - Stampede
  flex_slots:
  - Stampede
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Freya''s Tears, Amanita Charm, Jotunn''s
    Revenge, Kinetic Cuirass, Shield of the Phoenix, Hydra''s Lament, Soul Gem, Berserker''s
    Shield, Eye of Providence, Gluttonous Grimoire, Oni Hunter''s Garb, The Crusher,
    Screeching Gargoyle, Chronos'' Pendant, Spear of Desolation, Gladiator''s Shield,
    Chandra''s Grace, Erosion, Shield Splitter, Spectral Armor, Prophetic Cloak, Draconic
    Scale, Pharaoh''s Curse, Yogi''s Necklace, Helm of Radiance, Rod of Asclepius,
    Eye of the Storm, Gem of Focus, Arondight, Death Metal, Leviathan''s Hide, Midgardian
    Mail, Jade Scepter, Spear of the Magus, Stone of Binding, Hide of the Nemean Lion.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.72
      win: 0.53
      pick: 0.27
      fit: 0.48
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.65
      win: 0.58
      pick: 0.19
      fit: 0.48
    Runeforged Hammer:
      total: 0.56
      efficiency: 0.61
      win: 0.63
      pick: 0.26
      fit: 0.32
    Freya's Tears:
      total: 0.53
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.64
    Shifter's Shield:
      total: 0.56
      efficiency: 0.56
      win: 0.61
      pick: 0.49
      fit: 0.45
    Stampede:
      total: 0.55
      efficiency: 0.53
      win: 0.71
      pick: 0.03
      fit: 0.29
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Runeforged Hammer
  - Shifter's Shield
  - Stampede
  flex_slots:
  - Breastplate of Valor
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Berserker''s Shield, The Crusher, Jotunn''s
    Revenge, Amanita Charm, Gluttonous Grimoire, Kinetic Cuirass, Eye of Providence,
    Hydra''s Lament, Shield Splitter, Oni Hunter''s Garb, Freya''s Tears, Soul Gem,
    Golden Blade, Eye of the Storm, Lernaean Bow, Pharaoh''s Curse, Shield of the
    Phoenix, Avenging Blade, Death Metal, Spectral Armor, Erosion, The Reaper, Yogi''s
    Necklace, Draconic Scale, Spear of the Magus, Damaru, Shogun''s Ofuda, Leviathan''s
    Hide, Dominance, Heartseeker, Tekko-Kagi, The Cosmic Horror, Helm of Radiance,
    Rod of Asclepius, Midgardian Mail, Tyrfing.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.72
      win: 0.53
      pick: 0.27
      fit: 0.23
    Berserker's Shield:
      total: 0.53
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.36
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.65
      win: 0.58
      pick: 0.19
      fit: 0.23
    Runeforged Hammer:
      total: 0.58
      efficiency: 0.61
      win: 0.63
      pick: 0.26
      fit: 0.44
    Shifter's Shield:
      total: 0.56
      efficiency: 0.56
      win: 0.61
      pick: 0.49
      fit: 0.42
    Stampede:
      total: 0.55
      efficiency: 0.53
      win: 0.71
      pick: 0.03
      fit: 0.27
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Runeforged Hammer
  - Gluttonous Grimoire
  - Shifter's Shield
  - Stampede
  flex_slots:
  - Genji's Guard
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Gluttonous Grimoire, Amanita Charm,
    The Crusher, Jotunn''s Revenge, Kinetic Cuirass, Berserker''s Shield, Soul Gem,
    Eye of Providence, Oni Hunter''s Garb, Hydra''s Lament, Death Metal, Spear of
    the Magus, Shield Splitter, Freya''s Tears, The Cosmic Horror, Helm of Radiance,
    Rod of Asclepius, Shield of the Phoenix, Eye of the Storm, Spectral Armor, Erosion,
    Spear of Desolation, Jade Scepter, Yogi''s Necklace, Pharaoh''s Curse, Avenging
    Blade, Draconic Scale, Golden Blade, Obsidian Shard, Triton''s Conch, The Reaper,
    Lernaean Bow, Chronos'' Pendant, Leviathan''s Hide, Damaru, Ethereal Staff.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.72
      win: 0.53
      pick: 0.27
      fit: 0.23
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.65
      win: 0.58
      pick: 0.19
      fit: 0.23
    Runeforged Hammer:
      total: 0.57
      efficiency: 0.61
      win: 0.63
      pick: 0.26
      fit: 0.4
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.55
    Shifter's Shield:
      total: 0.56
      efficiency: 0.56
      win: 0.61
      pick: 0.49
      fit: 0.42
    Stampede:
      total: 0.55
      efficiency: 0.53
      win: 0.71
      pick: 0.03
      fit: 0.27
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Eye of Providence
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Kinetic Cuirass, Eye of Providence, Berserker''s
    Shield, Gluttonous Grimoire, Jotunn''s Revenge, Shield Splitter, Oni Hunter''s
    Garb, Freya''s Tears, The Crusher, Hydra''s Lament, Eye of the Storm, Shield of
    the Phoenix, Erosion, Draconic Scale, Spectral Armor, Pharaoh''s Curse, Avenging
    Blade, Soul Gem, Golden Blade, Leviathan''s Hide, Yogi''s Necklace, Death Metal,
    Midgardian Mail, Stone of Binding, Mantle Of Discord, Hide of the Nemean Lion,
    Helm of Radiance, Lernaean Bow, Rod of Asclepius, Shogun''s Ofuda, Magi''s Cloak,
    Damaru, Stampede, Ancile, Wyrmskin Hide.'
  slot_scores:
    Eye of Providence:
      total: 0.53
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.57
    Genji's Guard:
      total: 0.55
      efficiency: 0.72
      win: 0.53
      pick: 0.27
      fit: 0.31
    Berserker's Shield:
      total: 0.53
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.37
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.37
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.67
    Amanita Charm:
      total: 0.54
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.57
  starter: *id001
---
